add_library(owee SHARED owee.cpp oweeparser.cpp)
target_link_libraries(owee PRIVATE Fcitx5::Core)
set_target_properties(owee PROPERTIES PREFIX "")

install(TARGETS owee DESTINATION "${FCITX_INSTALL_LIBDIR}/fcitx5")

configure_file(owee-addon.conf.in owee-addon.conf @ONLY)
install(FILES "${CMAKE_CURRENT_BINARY_DIR}/owee-addon.conf"
        RENAME owee.conf
        DESTINATION "${FCITX_INSTALL_PKGDATADIR}/addon")

install(FILES owee.conf
        DESTINATION "${FCITX_INSTALL_PKGDATADIR}/inputmethod")

foreach(tam 256 64 32)
  install(FILES "${CMAKE_CURRENT_SOURCE_DIR}/../data/icons/fcitx-owee-${tam}.png"
          RENAME fcitx-owee.png
          DESTINATION "share/icons/hicolor/${tam}x${tam}/apps")
endforeach()
