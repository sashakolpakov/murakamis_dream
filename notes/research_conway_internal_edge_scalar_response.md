# A scalar response for the quartic on internal Conway edges

21 November 2026. Research note. Earlier finals and public manuscripts
remain unchanged.

The quartic source problem on \(p-1\) internal packets still has an
exact scalar dual. Its root term is now bilinear rather than linear,
but the original tensor normalization makes that term small enough
to preserve uniform convexity of the scalar-forced inner problems.
The outer response is a contraction in two real coordinates.

This does not eliminate the internal packets. It gives a
dimension-independent certificate for the final closing once its
internal response is controlled. No geometric rate or finite-exception
theorem is proved.

## 1. The original weighted root term

Use the prescribed-leaf restriction of the binary-skeleton theorem.
There are \(p\) binary products and \(p-1\) free full packets when
\(p\ge1\); the feasible set \(\mathcal D\) is their product of unit
balls in the full \(N\)-dimensional Newton space. The exact source
budget \(B=B_{\rm tot}\) and original markings are retained. Write
the clamped quartic as
\[
 E(u)=R(u)+|g(u)|^2,\qquad m=\min_{\mathcal D}E,\qquad
 B^2m\le |K_N|^2\le\gamma B^2m,\quad \gamma=\frac{197}{196}.
 \tag{1}
\]
Here \(R\) is the sum of all nonroot corridor costs. It is
nonnegative. The exact root-corridor formula is
\[
 g(u)=
 \frac{cP\,\Phi_{\rm top}(u_L,u_R)}
      {\sqrt{\,1+\sum_i\|cP_i\|^2\,}} .
 \tag{2}
\]
The row \(c\) is the normalized original closing; \(P,P_i\) are
the known products of normalized turns in that root corridor.
The inputs in (2) are either free packets or prescribed leaf-only
transports. The square root is positive. In particular its known
denominator has not been discarded or inserted into a new budget.

Put \(\sigma=1/16\). The norm bounds in the binary-skeleton theorem
give, on \(\mathcal D\),
\[
 |g|\le\sigma^2,\qquad
 \|Dg\|\le\sqrt2\,\sigma^2,\qquad
 \|D^2g\|\le\sigma^2,\qquad I\le D^2E\le3I.
 \tag{3}
\]
The derivatives are real derivatives for
\(\langle h,k\rangle_{\mathbb R}=\operatorname{Re}(h^*k)\).
The scalar \(g\) takes values in \(\mathbb C\), regarded as two
real coordinates. The derivative bounds follow from the coefficient
norm \(\sigma^2\) of the bilinear form in (2). A fixed input makes
the corresponding expression linear, or constant, and only improves
these bounds.

The original half-gradient step for this quartic has each free
packet in its \(33/256\) ball. There also exists a feasible field
\(a\) with
\[
                                R(a)=0.
 \tag{4}
\]
Indeed the true normalized forward packets satisfy every nonroot
corridor equation and the prescribed leaf transports. This field is
used only to prove (4); no unknown binary packet or knot value is
inserted in the coefficients of (1)--(2).

## 2. Uniform scalar-forced inner problems

For \(\lambda\in\mathbb C\), define
\[
 h(\lambda)=\min_{u\in\mathcal D}
             \{R(u)+2\operatorname{Re}(\bar\lambda g(u))\},
 \qquad q(\lambda)=h(\lambda)-|\lambda|^2 .
 \tag{5}
\]
The minimum exists for every \(\lambda\), by compactness. For
\(|\lambda|\le\sigma^2\), it has a unique interior minimizer
\(u(\lambda)\).

**Proof of the inner assertion.** Equation (3) implies
\[
 \|D^2|g|^2\|\le
       2\|Dg\|^2+2|g|\|D^2g\|\le6\sigma^4.
\]
Thus for the inner objective \(J_\lambda=R+2\operatorname{Re}(\bar\lambda g)\),
\[
 \mu I\le D^2J_\lambda\le(3+8\sigma^4)I,\qquad
                         \mu:=1-8\sigma^4>0 .
 \tag{6}
\]
To check the original ball constraints, its half-gradient step
differs from that of \(E\) by
\[
                     (Dg)^*(g-\lambda).
 \tag{7}
\]
The derivative of \(g\) in either of its at most two free input
packets has norm at most \(\sigma^2\). Therefore the correction
in each packet, separately, has norm at most \(2\sigma^4\).
All other packet corrections are zero. The step maps \(\mathcal D\)
strictly into packet balls of radius
\[
                         \frac{33}{256}+2\sigma^4<1.
 \tag{8}
\]
The Hessian interval (6) makes this step a contraction with factor
\[
                             \frac12+4\sigma^4<1 .
 \tag{9}
\]
Its unique fixed point is interior and stationary, hence is the
unique global inner minimum. The real implicit function theorem
gives a smooth response on a neighborhood of the scalar disk.
\(\square\)

Define the scalar response
\[
                              s(\lambda)=g(u(\lambda)).
 \tag{10}
\]
It maps \(|\lambda|\le\sigma^2\) into the same closed disk.
Writing \(H_\lambda=D^2J_\lambda(u(\lambda))\), implicit
differentiation gives the real \(2\times2\) matrix
\[
 Ds(\lambda)=-2Dg\,H_\lambda^{-1}(Dg)^*,\qquad
 \|Ds(\lambda)\|\le
       \vartheta:=\frac{4\sigma^4}{1-8\sigma^4}
                              =\frac1{16382}.
 \tag{11}
\]
This matrix is negative semidefinite. The response is a real smooth
map; no complex holomorphy is asserted.

## 3. The exact scalar dual and its gap

**Theorem.** The clamped quartic minimum is exactly
\[
 \boxed{\qquad
             m=\max_{\lambda\in\mathbb C}q(\lambda).
 \qquad}
 \tag{12}
\]
The maximizer is unique, lies in \(|\lambda|\le\sigma^2\), and
satisfies \(\lambda_*=s(\lambda_*)\). Iteration of \(s\) from
any point of that disk converges with factor at most \(\vartheta\).

**Proof.** For every feasible \(u\) and every \(\lambda\),
\[
 E(u)-\{J_\lambda(u)-|\lambda|^2\}
                              =|g(u)-\lambda|^2\ge0.
 \tag{13}
\]
Hence \(q(\lambda)\le m\). Let \(u_*\) be the unique interior
minimum of \(E\), and put \(\lambda_*=g(u_*)\). Its modulus
is at most \(\sigma^2\). The stationary equation for \(E\)
is exactly the stationary equation for \(J_{\lambda_*}\).
The convexity and interior assertion already proved show that
\(u_*=u(\lambda_*)\). Equality holds in (13) there, proving (12).

The function \(h\) is concave on the whole scalar plane because
it is an infimum of affine functions of \(\lambda\).
Subtracting \(|\lambda|^2\) makes \(q\) strictly concave, so
its maximizer is unique. On the disk,
\(\nabla q=2(s-\lambda)\); alternatively (11) directly gives
the unique fixed point and its contracting iteration. \(\square\)

At any exact inner response, the entire remaining primal-dual
gap is one complex scalar:
\[
 \boxed{\qquad
 q(\lambda)\le m\le E(u(\lambda)),\qquad
 E(u(\lambda))-q(\lambda)=|s(\lambda)-\lambda|^2.
 \qquad}
 \tag{14}
\]
Computing this response still solves for the \(p-1\) full packets.
The scalar identity is not a claim that those packets have been
replaced by two real unknowns.

## 4. A relative certificate for the original closing

The zero-residual fact (4) is useful here. Since \(D^2R\ge\mu I\),
the quadratic strong-convexity inequality at a field \(u\), tested
against its zero-cost minimum, gives
\[
                  R(u)\le\frac{\|\nabla R(u)\|^2}{2\mu}.
\]
At the exact inner response,
\(\nabla R=-2(Dg)^*\lambda\). Equations (3) and (11) imply
\[
                         R(u(\lambda))\le\vartheta|\lambda|^2.
 \tag{15}
\]

Suppose \(\lambda\ne0\), \(|\lambda|\le\sigma^2\), and
\[
 |s(\lambda)-\lambda|\le\epsilon|\lambda|,
                                    \qquad 0\le\epsilon<1/2 .
 \tag{16}
\]
Writing \(\delta=s-\lambda\) in (5) gives
\[
 \begin{aligned}
 q(\lambda)&=R(u(\lambda))+|\lambda|^2
                      +2\operatorname{Re}(\bar\lambda\delta)
                      \ge(1-2\epsilon)|\lambda|^2,\\
 E(u(\lambda))&\le
              [\vartheta+(1+\epsilon)^2]|\lambda|^2.
 \end{aligned}
\]
Combining with (1) and (14) proves
\[
 \boxed{\quad
 B^2(1-2\epsilon)|\lambda|^2
   \le |K_N|^2
   \le\gamma B^2[\vartheta+(1+\epsilon)^2]|\lambda|^2.
 \quad}
 \tag{17}
\]
Thus if a fixed construction has eventually nonzero scalar trials
\(\lambda_N\) satisfying (16) for a fixed \(\epsilon<1/2\),
and if \(2\pi N^{-1}\log(B|\lambda_N|)\to V\), then the original
full-sequence source has the same limit \(V\).
The ratio of \(|K_N|\) to \(B|\lambda_N|\) is bounded between
the two explicit positive square-root constants in (17).
No geometric construction of these trials or their response bound
is supplied here.

For \(p=1\), there are no free internal packets after the prescribed
leaf restriction. For \(p=0\), the linear-chain root formula likewise
has no optimization. In both cases take \(R=0\), with \(g\) the known
constant root-corridor value; (12)--(17) hold with the empty inner
problem and constant response. Their evaluation asserts no
asymptotic rate.

## 5. Why the actual source structure matters

Fixed degree and coercivity alone do not give this scalar dual.
Even the uniformly convex real quartic
\[
 R(x)=(x^2-1)^2,\quad g(x)=\sqrt3\,x,\quad
 E(x)=R(x)+|g(x)|^2=x^4+x^2+1
\]
has \(\min E=1\), whereas
\(\max_\lambda[\min_x(R+2\lambda g)-\lambda^2]=0\):
testing \(x=\pm1\) bounds that expression by
\(-2\sqrt3|\lambda|-\lambda^2\), with equality zero at
\(\lambda=0\). This is a counterexample to a generic optimization
inference, not a knot counterexample.

Here the small root map, residual convexity, zero-cost forward field
and source comparison come from the retained Conway normalization.
They provide the response estimates but no geometric exponential
rate by themselves. No dimension-independent bound on algebraic
elimination degree, and no complete elimination of the quantum
packets, is claimed. The theorem concerns the original \(p-1\)-packet
quartic; it does not assume that a further partial minimization
preserves its root-square decomposition.

## Complete proof source

The entire matching source is
[the quartic on internal Conway edges](research_conway_binary_skeleton_quartic.md),
SHA-256
\(\texttt{294220039d913fd349b867f9705670215c3ca98f581461c6f406db0dac20c7a3}\).
It supplies the exact corridor weights, original normalization,
source sandwich, Hessian bounds and inward step. The scalar assembly
and response estimates are proved above.

The complete proof source was read at the displayed matching pin.
Only written mathematics and text/hash operations were used. No
mathematical program, numerical experiment, test, build, git operation
or earlier-final edit was performed.
