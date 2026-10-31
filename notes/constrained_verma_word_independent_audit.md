# Independent audit of the constrained common-Verma word

Audit, 27 October 2026. The proof in
[constrained_verma_word_source_extension.md](constrained_verma_word_source_extension.md)
is sound, with the source-comparison qualification now explicit
in Section 4. No new tests were needed.

Each crossing preserves total integer index. Thus the chosen finite
ambient module has dimension \(\binom{bN}{b}\), contains the entire
head, and is invariant under every crossing of either sign. The
two opposite first-exit/first-return factors give the printed
\(\delta,w\) blocks. Only the \(m-1\) internal word times require
tail variables; discarded final tail output cannot affect the head
cut. This is a sufficient construction, not a minimal-rank claim.

The tail matrix \(F=I-D\) has strictly lower word-time \(D\), so its
inverse is a finite sum. Direct ordered block multiplication gives
\[
 U_FLV_F=\operatorname{diag}(E-\delta wBF^{-1}C,F).
\]
The memory entry \(b_jd_{j-1}\cdots d_{i+1}c_i\) records exactly
one tail visit. Each such visit advances time by at least two;
therefore the claimed finite excursion expansion and the bound
\(\lfloor m/2\rfloor\) are correct. The original finite word is
its zero-excursion coefficient, not the unrestricted ambient word.

For the constrained extension, the printed unipotent matrices
satisfy, over any associative ring and in the displayed order,
\[
 U\begin{pmatrix}A&B&0\\C&D&I\\0&I&0\end{pmatrix}V
       =\operatorname{diag}\!\left(A,
          \begin{pmatrix}0&I\\I&0\end{pmatrix}\right).
\]
This does not invert a wall, the head operator, or the tail
operator. The source map \(h\mapsto(h,0,\delta Ch)\), residual map
\(f\mapsto(f,0,0)\), and retraction
\((f,g,k)\mapsto f+wBk\) satisfy all stated chain identities.
The preserved cut is literally the original head functional.

Differentiating those whole chain identities gives the first-normal
cokernel formula. The terms involving the derivative of the
embedding lie in the special-fiber image, as required; the exact
whole identity also preserves all higher jets and the normal
co-source. A gauge carries the tail inclusion and projection
themselves, so their transformed projector retains its actual
irregular exponential. Keeping a regularized generator module
while deleting that projector would change the complex.

An important presentation distinction was clarified during this audit.
The cited scalar-to-companion construction has target
\(M=T^N-I\). That target is not automatically the word-time head
operator \(E\). Applying the conditional formula
\(K_{\mathrm{con}}(I_0J)=(I_1R)P\) to this actual word still requires a
supplied chain map \(EJ=RP\); alternatively the general algebraic
extension theorem can be applied directly with \(A=M\).
The revised note states this distinction explicitly and does not
claim to construct the missing actual quantum-A/network map.

The result is therefore a genuine whole pointed presentation of the
constrained finite word. It neither identifies the unconstrained
period with that word nor proves a geometric source, source-flatness,
or a physical large-level norm.
