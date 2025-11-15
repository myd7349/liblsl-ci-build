# liblsl-ci-build

Automated CI/CD pipelines for building [liblsl](https://github.com/sccn/liblsl) dynamic libraries across multiple platforms using GitHub Actions.

## Used by SharpLSL

During the packaging process of [SharpLSL](https://github.com/myd7349/SharpLSL), these liblsl binary archives are automatically downloaded and bundled into NuGet packages named SharpLSL.Native.[RID], where `[RID]` represents the runtime identifier of the specific platform. For more information on runtime identifiers, see the official [RID catalog](https://learn.microsoft.com/en-us/dotnet/core/rid-catalog).

Supported platforms:

### Android

- android-arm
- android-arm64
- android-x64
- android-x86

### iOS

- ios-arm64
- iossimulator-arm64
- iossimulator-x64

### Linux

- linux-arm
- linux-arm64
- linux-x64

### macOS

- osx
- osx-arm64
- osx-x64

### Windows

- win-arm64
- win-arm64-mt
- win-x64
- win-x64-mt
- win-x86
- win-x86-mt

If it does not include the `-mt` suffix, use the multithreaded, DLL-specific version of the runtime library.
 If it does include `-mt`, use the multithreaded, static version of the runtime library.

For more information on the differences between `/MD` and `/MT`, refer to the official documentation: [/MD, /MT, /LD (Use runtime library)](https://learn.microsoft.com/en-us/cpp/build/reference/md-mt-ld-use-run-time-library?view=msvc-170).

## License

MIT
