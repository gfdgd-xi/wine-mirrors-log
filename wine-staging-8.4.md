# 简述
Wine 8.4 已发布，用于在 Linux 和其他平台下运行 Windows 游戏和应用程序。Wine 8.4 具有重要意义，因为它是发布最初始的 Wayland 图形驱动程序代码的版本。

目前 Wine 8.4 中 “winewayland.drv” 的状态尚未为最终用户和游戏玩家准备好，仍处于早期阶段，正在进行开发。距离在原生 Wayland 支持之外再补充 (X) Wayland 支持，还需要很长一段时间，可能在 2024 年初发布的 Wine 9.0 稳定版能看到。

Wine 8.4 还对 IME 支持代码进行了清理、测试修复以及总共 51 个错误修复。单个双周开发版本的 50 多个错误修复是相当多的。这些修复会影响一系列游戏、应用程序和其他核心 Wine 问题。 

# 完整

The Wine development release 8.4 is now available.  
  
What's new in this release:  
  - Initial step of the Wayland graphics driver.  
  - Cleanups in IME support.  
  - A number of test fixes.  
  - Various bug fixes.  
  
The source is available at:  
  
  https://dl.winehq.org/wine/source/8.x/wine-8.4.tar.xz  
  
Binary packages for various distributions will be available from:  
  
  https://www.winehq.org/download  
  
You will find documentation on https://www.winehq.org/documentation  
  
You can also get the current source directly from the git  
repository. Check https://www.winehq.org/git for details.  
  
Wine is available thanks to the work of many people. See the file  
AUTHORS in the distribution for the complete list.  
  
----------------------------------------------------------------  
  
Bugs fixed in 8.4 (total 51):  
  
 - #7585   Thief: the dark project hangs on 'esc' keypress in game if X in 24bpp mode  
 - #47407  Hard Truck 2: King of The Road (GOG) movies aren't played  
 - #49266  Amazon Games installs but won't start (needs WindowsFormsApplicationBase startup code?)  
 - #51848  Multiple applications have very poor performance after 4261369e5d8 (Secondhand Lands, SPORE)  
 - #52912  t2embed:t2embed fails on Windows with the UTF-8 codepage  
 - #52948  gdi32:font - test_EnumFonts() fails on Arial Bold on Windows in Russian  
 - #53172  advapi32:registry - test_enum_value() has a pair of rare failures in UTF-8 system locales  
 - #53182  shell32:shelllink - A save(NULL, TRUE) fails randomly in test_load_save() on Wine  
 - #53236  d3d9:device - test_wndproc() sometimes gets an unexpected WM_DISPLAYCHANGE in Wine  
 - #53270  test_WSARecv() fails when using wow64 thunks [Wow64ApcRoutine() overwrites return value set by NtContinue()]  
 - #53488  The dxgi:dxgi output is too big on debiant  
 - #53526  kernel32:sync - test_timer_queue() occasionally fails to delete the timer on Windows 10  
 - #53528  ntdll:info - test_query_kerndebug() fails on Windows 8 to 10 1709  
 - #53818  foobar2000 v1.6 crashes shortly after startup on Wine 7.19 or higher  
 - #53974  d3drm:d3drm sometimes crashes after failing to create the IDirect3DRMDevice* interface in Wine  
 - #53975  d3drm:d3drm sometimes fails to create an immediate mode device in Wine  
 - #54003  vbscript:run sometimes fails on Windows UTF-8 locales  
 - #54008  d3d9:device sometimes fails to create a D3D object in Wine, crashes  
 - #54019  The 64-bit ntdll:wow64 fails on Windows 11  
 - #54020  The 32-bit ntdll:wow64 fails on Windows 11  
 - #54052  winhttp:notification times out randomly in Wine  
 - #54058  user32:input - test_ToAscii() fails in the Hindi UTF-8 locale  
 - #54078  ntdll:pipe - test_blocking() sometimes fails in Wine when the pipe is not signaled  
 - #54168  kernel32:console - test_wait() sometimes fails on Windows 8+  
 - #54298  d3d12:d3d12 - test_desktop_window() fails on Windows 10 1709  
 - #54299  d3d12:d3d12 - test_create_device() gets an unexpected 0 refcount on Windows 10 1909+  
 - #54313  HS_hevo_gc 8.8.1.1 fails to launch  
 - #54379  since wine 8.0 print doesn't work any more  
 - #54449  nethack crashes  
 - #54491  regedit/regproc.c - export_key() is unable to return TRUE  
 - #54495  Motorola Ready For Assistant does not start, needs ext-ms-win-networking-wlanapi-l1-1-0.dll  
 - #54504  dbghelp:dbghelp, ntdll:wow64 & psapi:psapi_main fail on Windows 11 due to notepad.exe path remapping  
 - #54505  psapi:psapi_main - The 64-bit test_EnumProcessModules() gets unexpected Notepad case on Windows 11  
 - #54506  psapi:psapi_main - The 64-bit test_EnumProcessModulesEx() gets pcs-6464 and pcs-6432 failures on Windows 11  
 - #54507  psapi:psapi_main - The 32-bit test_EnumProcessModulesEx() gets many pcs-3232 failures due to partial copy errors on Windows 11  
 - #54509  psapi:psapi_main - The 64-bit test_EnumProcessModules() gets unexpected third module on Windows 11  
 - #54531  jsproxy:jsproxy crashes on Windows 11  
 - #54539  Starcraft Remastered Game Initialization Failed  
 - #54553  mmdevapi:propstore - The 32-bit test_setvalue_on_wow64() fails on Windows 10 2004+  
 - #54563  The gif is displaying wrongly, with weird backgrounds of various colors  
 - #54593  gdi32:dc - The SetDeviceGammaRamp() tests fails on Windows 10 1909  
 - #54605  The 32-bit dbghelp:dbghelp cannot run on Windows <= 10 1607 due to IsWow64Process2() call  
 - #54617  KakaoTalk IM text edit window leaves artifacts when the text overflows and scroll bar appears  
 - #54621  Wine 8.3 64-bit is missing in the Debian bookworm repo  
 - #54637  riched20:txtsrv - test_TxGetNaturalSize fails if system GUI font's glyph widths are wider than expected by the test  
 - #54645  TextPad 9.1 installation fails in Wine 6 from Linux Mint repo  
 - #54649  windows.perception.stub:perception - Windows 10 1607 does not have ISpatialSurfaceObserverStatics2  
 - #54657  kernel32:loader - test_import_resolution() gets bad tls data on Windows 7  
 - #54663  ldp.exe crashes on unimplemented function wldap32.dll.ldap_set_dbg_flags  
 - #54669  imm32:imm32 - ime_install() fails in some locales on Windows  
 - #54690  ldp.exe crashes when attempting to connect to an invalid host  
  
----------------------------------------------------------------  
  
Changes since 8.3:  
  
Alex Henrie (5):  
      wldap32: Add ldap_set_dbg_flags stub.  
      wldap32: Replace bvfreeU with plain free.  
      wldap32: Handle null LDAPMessage in ldap_count_entries.  
      wldap32: Handle null LDAPMessage in ldap_parse_result.  
      comctl32/treeview: Ignore the lParam to WM_PRINTCLIENT and add tests.  
  
Alexandre Julliard (32):  
      ntdll/tests: Check the default stack information against the exe header.  
      ntdll/tests: Remove invalid instruction from KiUserExceptionDispatcher test.  
      ntdll/tests: Allow zero size return for NtQueryDirectoryObject on Wow64.  
      wow64: In system calls always return the status from Wow64SystemServiceEx.  
      wow64: Push a valid return address when calling KiRaiseUserExceptionDispatcher.  
      wow64: Keep track of APC stack frames, similarly to user callback frames.  
      wow64: Declare exported functions in winternl.h.  
      maintainers: Assume maintainership of ARM platforms.  
      ntdll: Always call Wow64PrepareForException when dispatching an exception.  
      server: Determine the native thread context flags on the client side.  
      ntdll: Pass the WoW context to the server on ARM64.  
      ntdll: Don't touch the top of the 32-bit thread stack.  
      wow64: Create the WOW64INFO structure.  
      wow64: Fixup Eip for breakpoint exceptions.  
      wow64: Don't update the exception address in raise_exception().  
      wow64: Implement Wow64RaiseException().  
      make_makefiles: Die when the git command fails.  
      gitlab: Add workaround for more strict git ownership check.  
      lcms2: Import upstream release 2.15.  
      faudio: Import upstream release 23.03.  
      ldap: Import upstream release 2.5.14.  
      tiff: Import upstream release 4.5.0.  
      ntdll: Fix some CPU information tests on ARM64.  
      ntdll: Implement the SystemProcessorBrandString query.  
      ntdll: Implement the SystemProcessorFeaturesInformation query.  
      wineboot: Use the SystemProcessorBrandString query instead of cpuid.  
      ntdll/tests: Handle another possible status when SystemProcessorFeaturesInformation is not supported.  
      ntdll/tests: Fix Wow64 tests failures on Windows 11 ARM64.  
      ntdll/tests: Update some todos that succeed with the new wow64 architecture.  
      ntdll: Implement NtWow64IsProcessorFeaturePresent().  
      wow64: Forward NtWow64IsProcessorFeaturePresent() to the CPU backend.  
      wineboot: Add processor features for supported WoW64 architectures on ARM64.  
  
Alexandros Frantzis (6):  
      winewayland.drv: Add initial driver stub.  
      winewayland.drv: Add initial unixlib stub.  
      winewayland.drv: Perform basic per-process Wayland initialization.  
      win32u: Allow drivers to set the null user driver.  
      winewayland.drv: Report basic monitor information.  
      winewayland.drv: Report all advertised monitor modes to Wine.  
  
Anton Baskanov (1):  
      ir50_32: Handle 24-bit output media type.  
  
Brendan Shanks (4):  
      kernel32: Implement GetFirmwareType().  
      loader: In macOS preloader, move the top-down allocations area down.  
      loader: In macOS preloader, stop using mincore() to test if a region is empty.  
      kernelbase: Implement DiscardVirtualMemory().  
  
Connor McAdams (17):  
      uiautomationcore: Implement IUIAutomation::Create{True,False}Condition.  
      uiautomationcore: Implement IUIAutomation::CreatePropertyCondition.  
      uiautomationcore: Implement IUIAutomation::CreateNotCondition.  
      uiautomationcore: Implement IUIAutomation::CreateOrCondition.  
      uiautomationcore: Implement IUIAutomation::get_ControlViewCondition.  
      uiautomationcore: Implement IUIAutomation::get_RawViewCondition.  
      uiautomationcore: Validate input arguments for IUIAutomationElement::GetCurrentPropertyValueEx.  
      uiautomationcore: Add support for element array properties in IUIAutomationElement::GetCurrentPropertyValueEx.  
      uiautomationcore: Implement IUIAutomation::CreateCacheRequest.  
      uiautomationcore/tests: Add tests for IUIAutomationElement caching methods.  
      uiautomationcore: Implement IUIAutomationElement::BuildUpdatedCache.  
      uiautomationcore: Add support for caching property values in UiaGetUpdatedCache.  
      uiautomationcore: Implement IUIAutomationCacheRequest::AddProperty.  
      uiautomationcore: Implement IUIAutomationElement::GetCachedPropertyValueEx.  
      uiautomationcore/tests: Add tests for IUIAutomationElement find methods.  
      uiautomationcore: Implement IUIAutomationElement::FindAll{BuildCache}.  
      uiautomationcore: Implement IUIAutomationElement::FindFirst{BuildCache}.  
  
Daniel Tang (3):  
      wintypes: Stub RoIsApiContractMajorVersionPresent().  
      wofutil: Stub WofIsExternalFile().  
      windows.networking: Stub DllGetActivationFactory().  
  
Davide Beatrici (12):  
      winealsa: Return STATUS_SUCCESS for unused unixlib functions.  
      winecoreaudio: Return STATUS_SUCCESS for unused unixlib functions.  
      wineoss: Return STATUS_SUCCESS for unused unixlib functions.  
      winepulse: Return STATUS_SUCCESS for unused unixlib functions.  
      mmdevapi: Query MemoryWineUnixFuncs virtual memory and store the resulting handle.  
      winepulse: Move process_attach and process_detach handling into mmdevapi.  
      mmdevapi: Use UTF-16 for client name in "test_connect_params" and "create_stream_params" structs.  
      mmdevapi: Move test_connect handling into mmdevapi.  
      winealsa: Use GetModuleFileName() instead of hardcoded module filename for registry key.  
      winecoreaudio: Use GetModuleFileName() instead of hardcoded module filename for registry key.  
      wineoss: Use GetModuleFileName() instead of hardcoded module filename for registry key.  
      winepulse: Use GetModuleFileName() instead of hardcoded module filename for registry key.  
  
Derek Lesho (2):  
      mfplat/tests: Test bytestream closing behavior in IMFMediaSource::Shutdown.  
      winegstreamer/media_source: Close bytestream in ::Shutdown.  
  
Dmitry Timoshkov (2):  
      win32u: Give full access rights to the process window station.  
      win32u: Give full access rights to the thread desktop.  
  
Eric Pouech (10):  
      dbghelp/tests: Better use global variables.  
      dbghelp/tests: Preserve last error in process_get_kind().  
      dbghelp: Use 'wine' as loader on multi-arch configuration.  
      dbghelp/tests: Add tests for SymRefreshModuleList() on non-live target.  
      dbghelp: Don't set ELF loader when wine's loader isn't accessible.  
      dbghelp: Fix vdso.so lookup.  
      ntdll/tests: Use msinfo32.exe instead of notepad.exe.  
      ntdll/tests: Use msinfo32.exe instead of notepad.exe.  
      psapi/tests: Use msinfo32.exe instead of notepad.exe.  
      dbghelp/tests: Use msinfo32.exe instead of notepad.exe.  
  
Evan Tang (4):  
      ntdll: Fix inverted TlsIndex check.  
      kernel32/tests: Add test verifying that tls init functions are called.  
      ntdll/tests: Move TlsIndex test to kernel32:loader.  
      kernel32/tests: Fix tls callback tests on Windows 7.  
  
Fan WenJie (3):  
      opengl32: Fix missing conversion of glUnmapBuffer_params from 32bit to 64bit.  
      opengl32: Fix missing conversion of glUnmapNamedBuffer_params from 32bit to 64bit.  
      wow64: Fix missing conversion of ThreadWineNativeThreadName in wow64_NtSetInformationThread.  
  
Florian Will (1):  
      comdlg32/tests: Fix itemdlg tests on Windows.  
  
François Gouget (18):  
      advapi32/tests: Fix the RegEnumValueA() tests in UTF-8 locales.  
      msado15: Fix the spelling of a comment.  
      winscard: Fix the spelling of a function parameter.  
      riched20/tests: Fix a typo in a comment.  
      dbghelp/tests: Let the tests run on Windows 7, 8 and 10 <= 1607.  
      t2embed/tests: Fix the TTGetEmbeddingType() test in UTF-8 locales.  
      windows.perception.stub/tests: Skip some tests when ISpatialSurfaceObserverStatics2 is not supported.  
      vbscript/tests: Fix the testChrError() tests in the mixed locale case.  
      d3d8/tests: Remove an unused call to IDirect3D8_GetAdapterDisplayMode().  
      wofutil: Add a trailing linefeed to a FIXME().  
      dinput/tests: Skip the tests if acquiring the device fails.  
      advapi32/tests: Improve the resume handle service tests.  
      advapi32/tests: Better account for starting and stopping services.  
      advapi32/tests: Separate the EnumServicesStatus() and EnumServicesStatusEx() tests.  
      advapi32/tests: Better check the EnumServicesStatusExW() output.  
      advapi32/tests: Take into account service start / stop race conditions.  
      advapi32/tests: Enumerate the services using the Unicode API.  
      advapi32/tests: Skip some tests if the EventLog service crashed.  
  
Gabriel Ivăncescu (10):  
      kernel32: Fix GetNumberFormatA when input length is 0.  
      kernel32: Fix GetCurrencyFormatA when input length is 0.  
      mshtml: Hold ref to HTMLDocumentObj when calling external code.  
      mshtml: Hold ref to inner window when calling external code.  
      mshtml: Hold ref to outer window when navigating.  
      mshtml: Check if browser was detached during notifications while navigating.  
      mshtml: Hold ref to the frame element during readyState notifications.  
      mshtml: Grab refs to windows upfront before sending pagehide events.  
      mshtml: Use already available window local variable in refresh task.  
      jscript: Fix jsstr leak after changing variant type to BSTR.  
  
Georg Lehmann (5):  
      winevulkan: Deal with per api xml entries.  
      winevulkan: Only parse extensions for Vulkan.  
      winevulkan: Skip features that are not part of Vulkan.  
      winevulkan: Add basic support for extension dependencies.  
      winevulkan: Update to VK spec version 1.3.242.  
  
Giovanni Mascellani (5):  
      d3d12/tests: Test that D3D12 swapchains can only be created on direct command queues.  
      dxgi: Immediately error out when creating a D3D12 swapchain on a non-immediate queue.  
      dxgi: Always assume that a D3D12 swapchain always uses user images.  
      dxgi/tests: Test that ResizeBuffers() resets the back buffer index to zero.  
      dxgi: Reset the back buffer index to zero on ResizeBuffers().  
  
Hans Leidekker (1):  
      adsldp/tests: Skip all remaining tests when the server is down.  
  
Henri Verbeet (11):  
      wined3d: Don't bother explicitly terminating the GLSL info log in print_glsl_info_log().  
      wined3d: Use wined3d_get_line() in shader_glsl_compile().  
      wined3d: Use wined3d_get_line() in shader_glsl_dump_program_source().  
      wined3d: Use wined3d_get_line() in shader_arb_compile().  
      wined3d: Use wined3d_get_line() in shader_spirv_compile_shader().  
      wined3d: Use wined3d_get_line() in shader_spirv_scan_shader().  
      d3d11: Get rid of the DXBC tag definitions.  
      wined3d: Sort the exports.  
      d3dcompiler: Handle some newer D3D_BLOB_PART values in debug_d3dcompiler_d3d_blob_part().  
      wined3d: Get rid of the wined3d_shader_byte_code_format enum.  
      wined3d: Use vkd3d-shader to disassemble shaders.  
  
Hugh McMaster (2):  
      regedit: Allow export_key() to return TRUE.  
      regedit: Append '.reg' file extension if necessary.  
  
Huw D. M. Davies (1):  
      winedump: Fix printf format warning.  
  
Jacek Caban (1):  
      winedump: Print static lib EC symbols.  
  
Jinoh Kang (4):  
      riched20/tests: Test for ITextDocument::Freeze and ITextDocument::Unfreeze.  
      riched20: Don't assume that TxDraw preserves the device context's brush selection.  
      riched20: Implement ITextDocument::Freeze and ITextDocument::Unfreeze.  
      riched20/tests: Don't specify DT_WORDBREAK in _check_txgetnaturalsize().  
  
Martin Storsjö (1):  
      ntdll: Handle aarch64 pointer authentication in unwind info.  
  
Max Figura (20):  
      wined3d: Move the WINED3D_RS_WRAP12 stub to wined3d_device_apply_stateblock.  
      wined3d: Move the WINED3D_RS_WRAP11 stub to wined3d_device_apply_stateblock.  
      wined3d: Move the WINED3D_RS_WRAP10 stub to wined3d_device_apply_stateblock.  
      wined3d: Move the WINED3D_RS_WRAP9 stub to wined3d_device_apply_stateblock.  
      wined3d: Move the WINED3D_RS_WRAP8 stub to wined3d_device_apply_stateblock.  
      wined3d: Move the WINED3D_RS_WRAP7 stub to wined3d_device_apply_stateblock.  
      wined3d: Move the WINED3D_RS_WRAP6 stub to wined3d_device_apply_stateblock.  
      wined3d: Move the WINED3D_RS_WRAP5 stub to wined3d_device_apply_stateblock.  
      wined3d: Move the WINED3D_RS_WRAP4 stub to wined3d_device_apply_stateblock.  
      wined3d: Move the WINED3D_RS_WRAP3 stub to wined3d_device_apply_stateblock.  
      wined3d: Move the WINED3D_RS_WRAP2 stub to wined3d_device_apply_stateblock.  
      wined3d: Move the WINED3D_RS_WRAP1 stub to wined3d_device_apply_stateblock.  
      wined3d: Move the WINED3D_RS_WRAP0 stub to wined3d_device_apply_stateblock.  
      wined3d: Move the WINED3D_RS_EXTENTS stub to wined3d_device_apply_stateblock.  
      wined3d: Move the WINED3D_RS_COLORKEYBLENDENABLE stub to wined3d_device_apply_stateblock.  
      wined3d: Move the WINED3D_RS_SOFTWAREVERTEXPROCESSING stub to wined3d_device_apply_stateblock.  
      wined3d: Move the WINED3D_RS_PATCHEDGESTYLE stub to wined3d_device_apply_stateblock.  
      wined3d: Move the WINED3D_RS_PATCHSEGMENTS stub to wined3d_device_apply_stateblock.  
      wined3d: Move the WINED3D_RS_DEBUGMONITORTOKEN stub to wined3d_device_apply_stateblock.  
      wined3d: Move the WINED3D_RS_INDEXEDVERTEXBLENDENABLE stub to wined3d_device_apply_stateblock.  
  
Mohamad Al-Jaf (22):  
      include: Add windows.perception.spatial.idl file.  
      include: Add windows.graphics.directx.idl file.  
      include: Add windows.perception.spatial.surfaces.idl file.  
      windows.perception.stub: Add stub DLL.  
      windows.perception.stub: Add ISpatialSurfaceObserverStatics stub interface.  
      windows.perception.stub: Add ISpatialSurfaceObserverStatics2 stub interface.  
      windows.perception.stub/tests: Add ISpatialSurfaceObserverStatics2::IsSupported() tests.  
      windows.perception.stub: Implement ISpatialSurfaceObserverStatics2::IsSupported().  
      pdh: Implement PdhVbGetDoubleCounterValue().  
      pdh/tests: Add PdhVbGetDoubleCounterValue() tests.  
      include: Add windows.graphics.directx.direct3d11.idl file.  
      include: Add Windows.Foundation.Deferral definition.  
      include: Add windows.graphics.holographic.idl file.  
      include: Add IHolographicSpaceStatics2 interface definition.  
      windows.perception.stub: Add IHolographicSpaceStatics2 stub interface.  
      windows.perception.stub/tests: Add IHolographicSpaceStatics2 properties tests.  
      windows.perception.stub: Implement IHolographicSpaceStatics2::get_IsSupported().  
      windows.perception.stub: Implement IHolographicSpaceStatics2::get_IsAvailable().  
      include: Add IHolographicSpaceStatics3 interface definition.  
      windows.perception.stub: Add IHolographicSpaceStatics3 stub interface.  
      windows.perception.stub/tests: Add IHolographicSpaceStatics3::get_IsConfigured() tests.  
      windows.perception.stub: Implement IHolographicSpaceStatics3::get_IsConfigured().  
  
Paul Gofman (1):  
      winex11.drv: Don't allow changing internal pixel format if conflicts with non-internal.  
  
Piotr Caban (4):  
      gdiplus: Use transparency instead of background color if transparent color flag is set in GIF GCE.  
      gdi32: Improve EMR_CREATEDIBPATTERNBRUSHPT playback.  
      wineps: Fix buffer overflow in PSDRV_WriteDIBPatternDict function.  
      wineps: Fix image bits access in PSDRV_WriteDIBPatternDict.  
  
Rémi Bernon (89):  
      win32u: Initialize IO_STATUS_BLOCK in load_directory_fonts.  
      win32u: Initialize IO_STATUS_BLOCK in rawinput add_device.  
      winex11: Initialize IO_STATUS_BLOCK in X11DRV_GetICMProfile.  
      maintainers: Assume maintainership of IME support.  
      imm32/tests: Add broken test results for w10v22H2.  
      makedep: Rename TESTDLL generated .res to avoid conflicts.  
      makedep: Support resource files for embedded TESTDLL.  
      imm32/tests: Test ImmInstallIMEW with an actual IME.  
      imm32/tests: Redirect IME function to the main module.  
      imm32/tests: Test ImmGetDescription with the installed IME.  
      imm32/tests: Test ImmGetIMEFileName with the installed IME.  
      user32/tests: Skip tests if layout failed to activate.  
      user32/tests: Add a WM_INPUTLANGCHANGE message test.  
      win32u: Move window query functions around.  
      win32u: Send WM_INPUTLANGCHANGE when activating new layout.  
      imm32: Implement stubs for ImmFreeLayout and ImmLoadIME.  
      imm32/tests: Test undocumented ImmLoadIME / ImmFreeLayout.  
      imm32: Rename ImmHkl to struct ime.  
      imm32: Reorder control flow in ImmConfigureIMEA.  
      imm32: Reorder control flow in ImmConfigureIMEW.  
      imm32: Reorder control flow in ImmEnumRegisterWordA.  
      imm32: Reorder control flow in ImmEnumRegisterWordW.  
      imm32: Reorder control flow in ImmEscapeA.  
      imm32: Reorder control flow in ImmEscapeW.  
      imm32: Reorder control flow in ImmGetConversionListA.  
      imm32: Reorder control flow in ImmGetConversionListW.  
      imm32: Reorder control flow in ImmGetProperty.  
      imm32: Reorder control flow in ImmGetRegisterWordStyleA.  
      imm32: Reorder control flow in ImmGetRegisterWordStyleW.  
      imm32: Reorder control flow in ImmRegisterWordA.  
      imm32: Reorder control flow in ImmRegisterWordW.  
      imm32: Reorder control flow in ImmUnregisterWordA.  
      imm32: Reorder control flow in ImmUnregisterWordW.  
      imm32: Reorder control flow in ImmGetImeMenuItemsA.  
      imm32: Reorder control flow in ImmGetImeMenuItemsW.  
      imm32: Avoid casts when calling into A/W IME.  
      imm32: Fail to load IME on any missing entry.  
      imm32: Return early if IMM_GetImmHkl fails.  
      imm32: Move IMM_FreeThreadData helper around.  
      imm32: Rename input context immKbd to ime.  
      imm32: Implement ImmLoadIME and ImmFreeLayout.  
      imm32: Rename some struct ime members.  
      imm32: Delete unnecessary uSelected struct ime member.  
      imm32: Use a single ime_is_unicode helper.  
      win32u: Keep the current user locale when enumerating layouts.  
      win32u: Keep the current user locale when loading layout.  
      win32u: Prevent user locale change in NtUserActivateKeyboardLayout.  
      winex11: Remove now unnecessary user locale change checks.  
      widl: Use explicit %empty token for empty rules.  
      widl: Add missing rule end semicolons.  
      widl: Use noyywrap lexer option.  
      widl: Use bison-bridge option.  
      widl: Remove unused temp_name member.  
      imm32: Rename szImeRegFmt to layouts_formatW.  
      imm32: Transform "Ime File" value in ImmInstallIMEW.  
      imm32: Rewrite ImmGetIMEFileName(A|W).  
      imm32: Rewrite ImmGetDescription(A|W).  
      imm32: Use CRT allocation functions.  
      widl: Use a struct list to keep imported files.  
      widl: Simplify handling of already parsed imports.  
      widl: Use a struct list for the import stack.  
      widl: Handle preprocess-only case separately.  
      widl: Introduce new (open|close)_input_file helpers.  
      widl: Respect -N flag for imported files preprocessing.  
      widl: Use open_input_file to open the main input.  
      imm32/tests: Use LANG_INVARIANT for the installed IME.  
      imm32/tests: Test ImmIsIME with the installed IME.  
      imm32/tests: Test ImmGetProperty with the installed IME.  
      imm32/tests: Test ImmEscape with the installed IME.  
      imm32/tests: Test ImmEnumRegisterWord with the installed IME.  
      imm32/tests: Test ImmRegisterWord with the installed IME.  
      imm32/tests: Test ImmGetRegisterWordStyle with the installed IME.  
      imm32/tests: Test ImmUnregisterWord with the installed IME.  
      imm32/tests: Test basic ImmEnumInputContext usage.  
      include: Add some dinput.h action semantics definitions.  
      dinput/tests: Test BuildActionMap / SaveActionMap with the HID joystick.  
      dinput/tests: Test SaveActionMap effect on DIPROP_USERNAME property.  
      dinput/tests: Test SaveActionMap effect on DIPROP_APPDATA property.  
      dinput/tests: Test SaveActionMap effect on DIPROP_BUFFERSIZE property.  
      dinput/tests: Test SaveActionMap effect on DIPROP_RANGE property.  
      dinput/tests: Test SaveActionMap effect on HID joystick input.  
      dinput/tests: Remove BuildActionMap / SaveActionMap mouse and keyboard tests.  
      dinput/tests: Increase timeouts for waits not supposed to fail.  
      widl: Group <INITIAL,ATTR> tokens together.  
      widl: Group <INITIAL> tokens together.  
      widl: Group <ATTR> tokens together.  
      widl: Introduce a new helper to produce num tokens.  
      widl: Simplify string literals lexing.  
      widl: Avoid freeing input_name in pop_import.  
  
Stefan Dösinger (7):  
      dxgi/tests: Fix UnregisterClass call in test_resize_target_wndproc.  
      dxgi/tests: Run test_resize_target_wndproc on d3d12 too.  
      dxgi/tests: Run test_swapchain_window_messages on d3d12.  
      dxgi: Unlock the wined3d mutex after storing the new target.  
      dxgi: Catch nested SetFullscreenState invocations.  
      dxgi/tests: Test nested fullscreen application from different thread.  
      dxgi/tests: Test nested SetFullscreenState from the same thread.  
  
Sven Baars (12):  
      kernelbase: Pass the root key to open_key().  
      kernelbase: Pass the key name to open_key().  
      kernelbase: Pass the root key to create_key().  
      kernelbase: Pass the key name to create_key().  
      kernelbase: Restructure the open_key() loop.  
      kernelbase: Always try to open the Wow6432Node in open_key().  
      kernelbase: Factor opening a subkey out of open_key().  
      kernelbase: Move create_key() below open_key().  
      kernelbase: Add a fast path to create_key().  
      kernelbase: Restructure the create_key() loop.  
      advapi32/tests: Test deleting 32-bit registry keys.  
      kernelbase: Also call NtOpenKeyEx() on empty key names.  
  
Zebediah Figura (24):  
      ddraw: Move pitch validation to ddraw_surface_create_wined3d_texture().  
      ddraw: Separate a need_draw_texture() helper.  
      ddraw: Restructure ddraw_surface_create_wined3d_texture() to avoid gotos.  
      ddraw: Move the wined3d_texture_update_desc() call into ddraw_surface_create_wined3d_texture().  
      ddraw: Move wined3d_resource_desc translation to ddraw_surface_create_wined3d_texture().  
      win32u: Make NtUserSetWindowPixelFormat() into a proper export.  
      win32u: Introduce a win32u_get_window_pixel_format() helper.  
      winex11: Retrieve the pixel format from win32u for normal windows in wglGetPixelFormat().  
      wineandroid: Retrieve the pixel format from win32u for normal windows in wglGetPixelFormat().  
      winemac: Retrieve the pixel format from win32u for normal windows in wglGetPixelFormat().  
      wined3d: Do not set the pixel format if wglGetPixelFormat() returns zero and we already set the internal pixel format.  
      win32u: Allow separately storing the internal pixel format set by WGL_WINE_pixel_format_passthrough.  
      winex11: Separately store the internal pixel format set by WGL_WINE_pixel_format_passthrough.  
      winemac: Separately store the internal pixel format set by WGL_WINE_pixel_format_passthrough.  
      wineandroid: Separately store the internal pixel format set by WGL_WINE_pixel_format_passthrough.  
      dxgi: Call wined3d_swapchain_state_set_fullscreen in d3d12_swapchain_init.  
      ddraw: Rename "is_complex_root" to "is_root".  
      ddraw: Remove some outdated comments from ddraw_surface7_SetSurfaceDesc().  
      ddraw: Move sysmem_fallback setting to ddraw_surface_create_wined3d_texture().  
      ddraw: Factor out more common initialization into ddraw_surface_create_wined3d_texture().  
      ddraw: Move sub-resource surface initialization to ddraw_surface_create_wined3d_texture().  
      ddraw: Move the rest of the surface desc population to ddraw_surface_create() from device_parent_texture_sub_resource_created().  
      ddraw: Do not return a wined3d_texture from ddraw_surface_create_wined3d_texture().  
      ddraw: Rename ddraw_surface_create_wined3d_texture() to ddraw_texture_init().  
  
Zhiyi Zhang (4):  
      gitlab: Make FVWM respect position hints.  
      user32/tests: Do not modify cursor position when simulating clicks.  
      light.msstyles: Add nonclient metrics.  
      user32/tests: Test winstation and desktop access rights.