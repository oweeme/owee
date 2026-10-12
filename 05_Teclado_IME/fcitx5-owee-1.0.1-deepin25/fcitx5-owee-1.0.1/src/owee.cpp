#include "owee.h"
#include "oweeparser.h"

#include <fcitx/instance.h>
#include <fcitx/inputpanel.h>
#include <fcitx/userinterfacemanager.h>
#include <cctype>

void OweeState::reset() {
    buffer_.clear();
    updateUI();
}

bool OweeState::commit(bool trailingSpace) {
    if (buffer_.empty()) return false;

    const std::string roman = buffer_.userInput();
    auto script = owee::romanWordToScript(roman);

    // Invalid Owee word: keep Roman text so the user never loses input.
    ic_->commitString(script ? *script : roman);
    if (trailingSpace) ic_->commitString(" ");

    buffer_.clear();
    updateUI();
    return true;
}

void OweeState::updateUI() {
    auto &panel = ic_->inputPanel();
    panel.reset();

    if (!buffer_.empty()) {
        // Roman Owee is intentionally shown during composition.
        if (ic_->capabilityFlags().test(fcitx::CapabilityFlag::Preedit)) {
            fcitx::Text preedit(buffer_.userInput(),
                                fcitx::TextFormatFlag::HighLight);
            panel.setClientPreedit(preedit);
        } else {
            panel.setPreedit(fcitx::Text(buffer_.userInput()));
        }
    }

    ic_->updateUserInterface(fcitx::UserInterfaceComponent::InputPanel);
    ic_->updatePreedit();
}

void OweeState::keyEvent(fcitx::KeyEvent &event) {
    if (buffer_.empty()) {
        auto sym = event.key().sym();
        if (sym < FcitxKey_A || sym > FcitxKey_z) return;
    }

    if (!buffer_.empty()) {
        if (event.key().check(FcitxKey_BackSpace)) {
            buffer_.backspace();
            updateUI();
            return event.filterAndAccept();
        }

        if (event.key().check(FcitxKey_Escape)) {
            reset();
            return event.filterAndAccept();
        }

        if (event.key().check(FcitxKey_space)) {
            commit(true);
            return event.filterAndAccept();
        }

        if (event.key().check(FcitxKey_Return) ||
            event.key().check(FcitxKey_KP_Enter)) {
            commit(false);
            // Let Enter itself continue to the application after committing.
            return;
        }

        // Punctuation commits the current word first, then passes through.
        const auto sym = event.key().sym();
        if (!((sym >= FcitxKey_A && sym <= FcitxKey_Z) ||
              (sym >= FcitxKey_a && sym <= FcitxKey_z))) {
            commit(false);
            return;
        }
    }

    const auto sym = event.key().sym();
    if ((sym >= FcitxKey_A && sym <= FcitxKey_Z) ||
        (sym >= FcitxKey_a && sym <= FcitxKey_z)) {
        char c = static_cast<char>(sym);
        c = static_cast<char>(std::tolower(static_cast<unsigned char>(c)));
        buffer_.type(c);
        updateUI();
        return event.filterAndAccept();
    }
}

OweeEngine::OweeEngine(fcitx::Instance *instance)
    : instance_(instance),
      factory_([this](fcitx::InputContext &ic) {
          return new OweeState(this, &ic);
      }) {
    instance_->inputContextManager().registerProperty("oweeState", &factory_);
}

void OweeEngine::keyEvent(const fcitx::InputMethodEntry &entry,
                          fcitx::KeyEvent &event) {
    FCITX_UNUSED(entry);

    // Key releases and modified shortcuts (Ctrl+C, Alt+Tab...) pass through.
    if (event.isRelease() || event.key().states()) return;

    auto *state = event.inputContext()->propertyFor(&factory_);
    state->keyEvent(event);
}

void OweeEngine::reset(const fcitx::InputMethodEntry &,
                       fcitx::InputContextEvent &event) {
    event.inputContext()->propertyFor(&factory_)->reset();
}

fcitx::AddonInstance *
OweeEngineFactory::create(fcitx::AddonManager *manager) {
    return new OweeEngine(manager->instance());
}

FCITX_ADDON_FACTORY(OweeEngineFactory);
