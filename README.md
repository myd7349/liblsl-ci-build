# liblsl-ci-build

Automated CI/CD for building [liblsl](https://github.com/sccn/liblsl) dynamic link libraries across multiple platforms using GitHub Actions.

## Used by SharpLSL

During the [SharpLSL](https://github.com/myd7349/SharpLSL) packaging process, these liblsl binary archives are downloaded automatically and packaged into NuGet packages named SharpLSL.Native.[rid]. Here, `[rid]` represents the runtime identifier for the specific platform. For details on runtime identifiers, refer to the [RID catalog](https://learn.microsoft.com/en-us/dotnet/core/rid-catalog).

Android:

- android-arm
- android-arm64
- android-x64
- android-x86

iOS:

- ios-arm64
- iossimulator-arm64
- iossimulator-x64

Linux:

- linux-arm
- linux-arm64
- linux-x64

macOS:

- osx
- osx-arm64
- osx-x64

Windows:

- win-arm64
- win-x64
- win-x86

## License

MIT
