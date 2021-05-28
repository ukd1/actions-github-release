# GitHub Actions: Get Github release
This Action able to get release details of private Github repos.

## Configuration

### Inputs

Name | Description | Example | Default
--- | --- | ---
repository | The Github owner/repository | `nodejs/node` | none
type | The release type (prerelease or stable) | `stable` | `latest`
token | Github auth token (default variable for each aciton session) | `${{ secrets.GITHUB_TOKEN }}` | `${{ secrets.GITHUB_TOKEN }}`

#### Possible values for `type` input
* *stable* - Get the stable `latest` release
* *prerelease* - Get the latest `prerelease`
* *latest* - Get the *really* latest release with no matter is it stable or prerelease

### Outputs
This action outputs the variables
- `release` with tag name of release.
- `release_tarball_url` with url of the tarball for that release.
- `release_zipball_url` with url of the zipball for that release.

## Usage example

```yaml
on:
  push:
    branches: [ main ]

jobs:
  build:
    name: Build
    runs-on: ubuntu-latest
    steps:
    
    - name: Get latest release of NodeJS
      uses: rez0n/actions-github-release@main
      id: node_release
      env:
        token: ${{ secrets.GITHUB_TOKEN }}
        repository: "nodejs/node"
        type: "stable"
        
    - name: Build image
      uses: docker/build-push-action@v1
        with:
          ...
          dockerfile: Dockerfile
          tags: latest, ${{ steps.node_release.outputs.release }}
```
