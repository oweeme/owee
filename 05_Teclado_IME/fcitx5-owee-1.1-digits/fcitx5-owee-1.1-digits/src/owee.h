#pragma once

#include <fcitx/addonfactory.h>
#include <fcitx/inputcontext.h>
#include <fcitx/inputmethodengine.h>
#include <fcitx/instance.h>
#include <fcitx/inputcontextmanager.h>
#include <fcitx-utils/inputbuffer.h>

class OweeEngine;

class OweeState : public fcitx::InputContextProperty {
public:
    OweeState(OweeEngine *engine, fcitx::InputContext *ic)
        : engine_(engine), ic_(ic) {}

    void keyEvent(fcitx::KeyEvent &event);
    void reset();
    void updateUI();

private:
    bool commit(bool trailingSpace);
    OweeEngine *engine_;
    fcitx::InputContext *ic_;
    fcitx::InputBuffer buffer_;
};

class OweeEngine : public fcitx::InputMethodEngineV2 {
public:
    explicit OweeEngine(fcitx::Instance *instance);

    void keyEvent(const fcitx::InputMethodEntry &entry,
                  fcitx::KeyEvent &event) override;
    void reset(const fcitx::InputMethodEntry &entry,
               fcitx::InputContextEvent &event) override;

    fcitx::Instance *instance() const { return instance_; }
    auto *factory() { return &factory_; }

private:
    fcitx::Instance *instance_;
    fcitx::FactoryFor<OweeState> factory_;
};

class OweeEngineFactory : public fcitx::AddonFactory {
public:
    fcitx::AddonInstance *create(fcitx::AddonManager *manager) override;
};
