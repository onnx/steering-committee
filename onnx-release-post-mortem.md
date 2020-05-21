# ONNX Release 1.7 Postmortem

## Release timelines

2/19/202: first release team sync-up meeting, and set initial targeted release date: 3/2/2020

3/9/2020: release candidate TestPypi (v1.7.102) created, however due to no training optimizers merged in master branch, release date was first revised to 3/31/2020, announced in gitter [https://gitter.im/onnx/Infra](https://gitter.im/onnx/Infra)

3/31/2020: release candidate TestPypi (v1.7.103) had issues identified by release verification team, release was delayed, discussed in gitter https://gitter.im/onnx/Infra

- issue 1: converters unable to produce functional models for release 1.7 with the incremented IR 7
- issue 2: sequence model has shape inference errors

4/6/2020: release candidate TestPypi (1.7.104) again had new issues identified by release verification team, release was delayed indefinitely, discussed in gitter https://gitter.im/onnx/Infra

 4/16/2020: decision to revert ops not ready for release, MeanSquareDistance, UnfoldToDepth, Inverse, Batchnorm update

 4/26/2020: operators identified with issues were patched with 7 PRs, SoftmaxCrossEntropyLoss, NegativeLogLikelihoodLoss, Celu, Dropout

 4/28/2020: &quot;preview domain&quot; concept was introduced and PR opened to move all training operators from training to preview domain, release was further delayed

 5/7/2020: release candidate TestPypi (1.7.105) approved by release verification team, release was delayed indefinitely, discussed in gitter

 5/8/2020: release builds (Linux, OSX, Windows) published to Pypi, [https://pypi.org/project/onnx/#files](https://pypi.org/project/onnx/#files), and v1.7.0 release and tag created in github, [https://github.com/onnx/onnx/releases/tag/v1.7.0](https://github.com/onnx/onnx/releases/tag/v1.7.0)

 5/11/2020: release builds (Linux, OSX) published to conda, [https://anaconda.org/conda-forge/onnx](https://anaconda.org/conda-forge/onnx)

 5/12/2020: release notes published to onnx.ai news, [http://onnx.ai/news.html](http://onnx.ai/news.html)

 5/14/2020: release announced in a LF AI blog, [https://lfai.foundation/blog/2020/05/14/onnx-1-7-now-available/](https://lfai.foundation/blog/2020/05/14/onnx-1-7-now-available/)




## Release process

1. Obtain credentials and permissions for all release related repos
2. Create release milestone and tag PRs to specify release scope and time frame
3. Update, fix, and verify release automation (wheel-builder and onnx-feedstock)
4. Upon release PRs all merged, create release branch and publish release candidate to TestPypi
5. Wait for release verification coming back clean
6. Build final release and publish to Pypi
7. Draft release change log and release notes
8. Create github release and tag
9. Publish to conda forge
10. Publish notes to onnx.ai news
11. Work with LFAI on release announcement and blog

##


## Release-related change log

###ONNX ([https://github.com/onnx/onnx](https://github.com/onnx/onnx))

PRs

- Add Windows pipelines since wheel-builder fails to build Windows python packages in AppVeyor, [https://github.com/onnx/onnx/pull/2632](https://github.com/onnx/onnx/pull/2632)
- Branch: rel-1.7.0
- Release: v1.7.0 with tag &quot;v1.7.0&quot;

### Wheel-builder (https://github.com/onnx/wheel-builder)

PRs

- Update dependency on multibuild version to fix a build issue, [https://github.com/onnx/wheel-builder/pull/21](https://github.com/onnx/wheel-builder/pull/21)

- Add python 3.8 builds, update version number, and set commit ID, [https://github.com/onnx/wheel-builder/pull/23](https://github.com/onnx/wheel-builder/pull/23)

- Release: v1.7.0 with tag




## Positive experiences

- The team is very quick to fix issues.
- The previous release manager Kevin is very helpful, providing instructions based on he had done for 1.6
- The infra SIG lead Ke is responsive in meeting requests and PR reviews and approvals
- The developers are very responsive to issues that blocked the release, especially Changming and Zeeshan
- Other people jumped in to help move release forward, Faith, Rama, Emad

## Issues

###Communication
- No formal communication channel for release scope, status, issues, and discussions. Ended up using onnx/infra gitter and a github issue.
- The onnx/releases gitter is inactive, last post Aug 31 2018
- Some people do not respond to release related questions. Even a quick &quot;I don&#39;t know&quot; or &quot;I don&#39;t have time to look into that&quot; would help.

### Release scope

- Initial scope, for ex. To include at least a training optimizer, was not totally communicated and fulfilled in a timely manner
- Additional fixes were requested to be added to the release
- IR version change was added late
- A few ops were removed very late
- New concept, preview domain, was added very late
- Unknown and undocumented exit criteria
- ONNX release seems to depend on passing tests that are not available or visible in ONNX core github.
- The owners of those tests are unknown making communication and problem resolution difficult.
- ONNX release seems to depend on certain converters

### Lack of up-to-date documentation for release process

- The release doc is helpful but not reflecting the current build process, https://github.com/onnx/onnx/blob/master/docs/OnnxReleases.md
- Utility projects out of date (wheel-builder, conda-forge/onnx-feedstock)
- wheel-builder had dependency issue
- wheel-builder failed to build Windows wheels
- onnx-feedstock has not been working for Windows for a year

### Readiness for release

- Many bugs were found during release verification process, not caught by approvers or CI.
- (Changming) Model checker doesn&#39;t detect shape inference errors, so many of the converter bugs were reported to onnxruntime project.
- (Changming 4/2) I found one more bug in the sequence op
- (Faith 4/2) The converter issue wasn&#39;t a prominent issue in the prior releases and we didn&#39;t detect it as ONNX Runtime was more relaxed on IR version constraints, but the latest version of ORT highlighted this.
- (Changming 4/3) It&#39;s because ONNX doesn&#39;t have a fully working model-checker, so it has to rely on onnxruntime&#39;s model checker to do it. If the op spec isn&#39;t finalized or fully validated it shoudn&#39;t be submitted to ONNX master branch.
- (Faith 4/3) Many issues were discovered late only when the tooling was updated to implement the changes.
- (Zeeshan, 4/4) What value does it add to release a spec without the op implementation in any runtime? The spec by itself seems useless.
- (Dmitri, 4/7) I understand that the excitement is running high due to the upcoming ONNX release. However, there are some outstanding issues with some specs in OpSet 12. I will focus on Inverse here…
- (Hariharan, 4/7) I also noticed another bug in the Einsum shape inference and filed an issue
- (Zeeshan, 4/13) It seems dropout-12 contains incorrect reference implementation and tests are wrong.
- (Negin, 4/14) I also have another bug fix for _shape inference_ of UnfoldToDepth
- (Zeeshan, 4/25) removes ~7 commits/4 ops from master branch in preparation for ONNX 1.7 release. The removal of these commits will give us the appropriate confidence level in the quality of ONNX 1.7 release

## What could be done for smoother future releases?

### Communication

- Provide guidelines on release communication, channel, roles, etc
- Tag issues and PRs with release milestone
- Be courteous and respectful

### Release scope

-What is the best way to define the release scope?
-What is the process to change the release scope?
-Who decides the change of release scope?

### Unknown and undocumented exit criteria

- Clearly define and document the release exit criteria
- Automate the release verification
- Maybe integrate the release verification with CI to eliminate the step of verification on release candidates?

### Utility projects out of date

- Dedicate release engineers to ensure release utility projects are up to date and functional
- Add Windows builds to wheel-builder
- Add Windows builds to onnx-feedstock
- Maintain the proper levels of dependencies in operating system, python, protobuf, etc

### Lack of up-to-date documentation for release process

- Update the release instructions

### Readiness for release

- Faith:Until the spec is adopted and used, it&#39;s liable to have issues that were not considered or were overlooked during the pure spec review. I think the first versions of any new operator or functionality is likely to have those regardless of how much diligence is put into the review and discussions, so it may be good to plan for this as part of the process for publishing updates._

- Zeeshan: Let&#39;s not make ONNX a scratch space. Before an op is submitted to ONNX we need to have its implementation that validated it against PT/TF. You start with the op implementation, validate it against PT/TF, then write the spec at the very end.

- Ke: Please do not take ONNX as an experimental place for op design.

- Clearly define the roles and dependencies between ONNX core, ONNX runtime, and ONNX converters
- Clearly define the requirements for a new or an updated operator to be approved and merged.
- Enhance tools, automation, and even docs to help ensure each new and updated operator has satisfied high quality standard.
- Enhance CI to catch issues before release time
