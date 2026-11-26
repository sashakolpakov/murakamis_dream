# An all-transfer logarithmic collar for the actual boundary Ward source

Written research proof, 23 November 2026.

The complete boundary Ward sum is one coefficient of an actual Euler
matrix times a finite logarithmic derivative. No inverse of a nilpotent
lowering operator is needed. On a coefficient circle approaching the
unit circle at distance of order \((\log\log N)/N\), that logarithmic
derivative has only its original vacuum kernel. After one literal
lowering shift and its explicit scale of order \(N\) are extracted, the
remaining matrix and its inverse have logarithmic and bounded norms.
A diagonal gauge with polylogarithmic conditioning extends inverse
control to the full unit activity disk. The physical degree grading
then extracts every Ward coefficient by a unitary Fourier projection,
with no small-activity
hypothesis and no additional coefficient-contour loss.

This controls an entire normal factor before geometric evaluation.
The original factorial, Euler matrix, crossing, marked co-source and
coefficient integral remain. No lower bound for that coefficient or
for the closed scalar is inferred.

## 1. The complete original Ward sum

Fix the original root and head count
\[
 N\ge2,\qquad d=N-1,\qquad q=e^{\pi i/N},\qquad Q=q^2,
 \qquad m=r+1\ge2,\qquad x_0=-q^{-1}.
 \tag{1}
\]
All norms below use the original physical Euclidean occupation basis
\(|a\rangle\), \(0\le a\le d\), and its tensor products. In particular
the actual first-remaining-head shift is
\[
 L|a\rangle=|a-1\rangle\quad(a>0),\qquad L|0\rangle=0,
 \qquad L^N=0,\qquad \|L\|=1.
 \tag{2}
\]
It acts as the identity on the other remaining heads. The ordered
remaining lowering coproduct is denoted by \(E\); its one-head
coefficient is \(Q^{-a}-1\), with the original bottom zero. Write
\(b=b_{\sigma_1}\) for the actual reduced positive boundary crossing,
including its crossing scalar. No framing factor is changed.

Let \(1\le t<N\) and let the actual physical weight satisfy
\(\lambda_0^2=Q^{-t}\). Put \(a=\lambda_0/x_0\); then \(|a|=1\).
Source [W, (19)--(20)] gives its complete flattened first-normal
arrow defect, with the fixed-root meridian derivative, as
\[
 \begin{split}
 \mathfrak D_t
 &=\sum_{n=1}^{t}\omega_{t,n}(\lambda_0)x_0^{-n}
                                      E^{t-n}bL^n,\\
 \omega_{t,n}(\lambda_0)
 &=2m(-1)^{n-1}\lambda_0^n{t\brack n}_Q F_{n-1},
 \qquad F_j=(Q;Q)_j,\quad F_0=1.
 \end{split}
 \tag{3}
\]
This is an equality of the original finite matrices, restricted to
the indicated input weight when defining the Ward arrow. We can also
form the displayed sum on the whole occupation space. Its order is
always \(E^{t-n}\), then \(b\), then \(L^n\). In particular no
commutation between these three operators is assumed.

Every factorial in (3) has index below \(N\). Its scalar coefficient
simplifies exactly to
\[
 \omega_{t,n}(\lambda_0)x_0^{-n}
 =2m(-1)^{n-1}a^n
       \frac{F_t}{F_{t-n}(1-Q^n)}
 =2m(-1)^{n-1}a^n
       \frac{(Q^{t-n+1};Q)_n}{1-Q^n}.
 \tag{4}
\]
There is no division by \(F_N\), and no transfer term has been
replaced by a fixed-\(n\) asymptotic.

For a nonself reciprocal pair, use its two physical orders \(t=s\)
and \(t=N-s\), at their corresponding input weights. The two defects
recover all four normal blocks of [W, (23)--(24)]. The construction
below acts on those complete defects before the original word-source
formula [W, (27)] is applied; its off-diagonal normal couplings remain.

## 2. A single coefficient and its finite logarithmic derivative

Define the native Euler polynomial and its logarithmic derivative
\[
 \mathcal E_N(z)=\sum_{j=0}^{d}\frac{z^j}{F_j},\qquad
 \ell_N(z)=\sum_{n=1}^{d}\frac{(-1)^{n-1}z^n}{1-Q^n}.
 \tag{5}
\]
Multiplication of finite polynomials, using (4), proves
\[
 \boxed{\quad
 \mathfrak D_t=2mF_t[\xi^t]\,
           \mathcal E_N(\xi E)\,b\,\ell_N(a\xi L).
 \quad}
 \tag{6}
\]
Indeed its term of degree \(\xi^t\) uses \(j=t-n\) and is
exactly the corresponding term of (3). This is also a homogeneous
polynomial in the commuting left- and right-multiplication operators
\(P(B)=EB\) and \(R(B)=aBL\). Neither \(E^{-1}\) nor \(L^{-1}\)
appears.

For completeness the logarithmic identity is finite algebra. In
\(\mathbb C[z]/(z^N)\), the Euler recurrence is
\[
 \mathcal E_N(Qz)=(1-z)\mathcal E_N(z),\qquad
 \log\mathcal E_N(z)=\sum_{n=1}^{d}\frac{z^n}{n(1-Q^n)}.
 \tag{7}
\]
The first formula follows by comparing coefficients. For the second,
take the formal logarithm with zero constant term: its degree-\(n\)
coefficient is determined by
\((Q^n-1)c_n=-1/n\). The Euler derivative \(z\partial_z\)
preserves the ideal \((z^N)\). Hence, with its sign specified,
\[
 \ell_N(z)=-z\partial_z\log\mathcal E_N(-z)
             =z\mathcal E_N'(-z)\mathcal E_N(-z)^{-1}
                                     \pmod {z^N}.
 \tag{8}
\]
Evaluation at \(z=a\xi L\) makes (7)--(8) exact matrix identities.
The inverse is a finite polynomial because \(L^N=0\). No analytic
logarithm or branch choice has been added. The same finite Euler
logarithm is covered by [C]; the new use here is (6) and the uniform
collar estimate below.

For any actual linear co-source \(\Lambda\) on this insertion, fixed
in \(\xi\), (6) gives the exact contraction formula
\[
 \Lambda(\mathfrak D_t)=\frac{2mF_t}{2\pi i}
   \oint_{|\xi|=\rho}
    \Lambda\!\left(\mathcal E_N(\xi E)b\ell_N(a\xi L)\right)
                            \frac{d\xi}{\xi^{t+1}},\qquad \rho>0.
 \tag{9}
\]
The contour extracts a coefficient of a finite polynomial. Its value
is independent of its positive radius. The input weight restriction
can be retained inside \(\Lambda\) throughout, as can the original
marked closing, exterior tensors and prescribed scalar lines when
this normal insertion occurs in them.

## 3. Normalizing the q-log factor

For \(T^N=0\), factor (5) exactly as
\[
 \ell_N(T)=\frac{1}{1-Q}\,T U_N(T),\qquad
 U_N(T)=\sum_{n=1}^{N-1}(-1)^{n-1}r_{N,n}T^{n-1},
 \quad r_{N,n}=\frac{1-Q}{1-Q^n}.
 \tag{10}
\]
The constant term of \(U_N\) is one. In particular it is invertible
at every nilpotent \(T\), but that observation alone would not bound
its inverse. Compare it to the finite resolvent integral
\[
 V(T)=\int_0^1(I+sT)^{-1}\,ds
      =\sum_{n=1}^{N}\frac{(-1)^{n-1}T^{n-1}}n.
 \tag{11}
\]
The term of degree \(N-1\) in (11) is retained; it is not present in
\(U_N\).

There is an absolute constant \(C\) such that
\[
 |r_{N,n}-1/n|\le C/N\quad(1\le n\le N/2),
 \qquad |r_{N,n}|\le\frac{C}{\min(n,N-n)}\quad(1\le n<N).
 \tag{12}
\]
To prove the first bound, let
\(g(s)=(e^{2\pi i s}-1)/(2\pi i s)\), continued by \(g(0)=1\).
It is continuously differentiable on \([0,1/2]\), and
\(|g(s)|\ge2/\pi\) there. Since
\(r_{N,n}=g(1/N)/(ng(n/N))\), the mean value bound gives
\(|r_{N,n}-1/n|\le C(n-1)/(nN)\le C/N\).
The second bound follows from
\(\sin(\pi n/N)\ge2\min(n,N-n)/N\) and
\(\sin(\pi/N)\le\pi/N\).

Consequently, for \(T^N=0\), \(\|T\|\le\rho\) and
\(0<\rho<1\), one has
\[
 \|U_N(T)-V(T)\|
 \le \frac{C}{N(1-\rho)}
       +C\rho^{N-1}\sum_{k=1}^{\lfloor N/2\rfloor}
                                      \frac{\rho^{-k}}k
       +\frac{2\rho^{N/2-1}}{N(1-\rho)}
       +\frac{\rho^{N-1}}N.
 \tag{13}
\]
For the lower half of the sum use the first bound in (12) and a
geometric series. In the upper half put \(k=N-n\), so
\(|r_{N,n}|\le C/k\), and bound the remaining \(1/n\) by
\(2/N\). The last term in (13) is precisely the last term of (11).
This proves the estimate for the complete polynomials, without
dropping a high-degree tail.

Choose the explicit collar
\[
                 \rho_N=\exp(-4\log\log N/N)
                         =(\log N)^{-4/N}.
 \tag{14}
\]
For all sufficiently large \(N\), writing
\(v_N=4\log\log N/N\) gives
\(v_N/2\le1-e^{-v_N}\le v_N\). Thus
\(1-\rho_N\) is comparable to \((\log\log N)/N\).
To estimate the second term of (13), put
\(K=\lfloor N/\log N\rfloor\). For \(k\le K\),
\(\rho_N^{-k}\le C\) and the harmonic sum is at most
\(C\log N\). For \(K<k\le N/2\), use
\(1/k\le C\log N/N\), at most \(N\) terms, and
\(\rho_N^{-k}\le(\log N)^2\). Since
\(\rho_N^{N-1}=\rho_N^{-1}(\log N)^{-4}\), the second term
of (13) is bounded by
\(C\{(\log N)^{-3}+(\log N)^{-1}\}\).
The third term is at most
\(C/\{(\log N)^2\log\log N\}\); the last is at most
\(C/\{N(\log N)^4\}\). The first is at most
\(C/\log\log N\). Therefore, uniformly for every \(T^N=0\)
with \(\|T\|\le\rho_N\),
\[
                    \|U_N(T)-V(T)\|\le C/\log\log N.
 \tag{15}
\]

## 4. Accretivity and the genuine remaining endpoint

If \(\|T\|\le\rho<1\), the resolvent in (11) satisfies
\[
 \operatorname{Re}(I+sT)^{-1}\ge\frac{I}{1+s\rho},
 \quad 0\le s\le1,
 \qquad
 \operatorname{Re}V(T)\ge\frac{\log(1+\rho)}\rho I
                                                    \ge(\log2)I.
 \tag{16}
\]
At \(\rho=0\) use the continuous value. Here is an elementary
operator proof of the first inequality. Put \(B=I+sT\) and
\(v=s\rho<1\). Then
\[
 (1+v)\operatorname{Re}B-B^\dagger B
   =vI-(1-v)s\operatorname{Re}T-s^2T^\dagger T\ge0,
\]
using \(\operatorname{Re}T\le\rho I\) and
\(T^\dagger T\le\rho^2I\). Congruence by \(B^{-1}\) gives
\((1+v)\operatorname{Re}B^{-1}\ge I\). Integration proves (16).
Also the Neumann resolvent estimate gives
\[
 \|V(T)\|\le\frac{-\log(1-\rho)}\rho.
 \tag{17}
\]
Combining (15)--(17), there are absolute constants \(C,N_0\)
such that for all \(N\ge N_0\) and all \(T^N=0\) with
\(\|T\|\le\rho_N\),
\[
 \boxed{\quad
 \operatorname{Re}U_N(T)\ge\tfrac12\log2\,I,\qquad
 \|U_N(T)^{-1}\|\le2/\log2,\qquad
 \|U_N(T)\|\le C\log N.
 \quad}
 \tag{18}
\]
Indeed accretivity bounds \(\|U_N(T)v\|\) below by
\((\log2)\|v\|/2\); in finite dimension this bounds the inverse.
All constants in (18) are independent of the number of tensor heads.

Now take the literal \(T=zL\). The factors in (10) commute, so
\[
 \ker\ell_N(zL)=\ker L,\qquad
 \operatorname{im}\ell_N(zL)=\operatorname{im}L\quad(z\ne0).
 \tag{19}
\]
These statements retain the original vacuum direction; no quotient
of the source is being taken. On \((\ker L)^\perp\), the shift
\(L\) is an isometry. Equations (10),(18) therefore bound the
nonzero singular values of \(\ell_N(zL)\) between
\(c|z|/|1-Q|\) and \(C|z|\log N/|1-Q|\).

More generally, for any compatible rectangular matrix \(B\), either
the physical operator norm or the Hilbert--Schmidt norm obeys
\[
 \frac{c|z|}{|1-Q|}\|BL\|
 \le\|B\ell_N(zL)\|
 \le\frac{C|z|\log N}{|1-Q|}\|BL\|,
 \qquad 0<|z|\le\rho_N,
 \tag{20}
\]
for \(N\ge N_0\). For the lower operator bound, write
\(BL=(BLU_N)U_N^{-1}\). For the Hilbert--Schmidt bound use
the least singular value of the right factor \(U_N\).
The upper bounds follow by multiplication. Thus every matrix on
the left is retained, including arbitrary exterior factors already
placed there. No analogous lower bound for an arbitrary scalar
co-source is asserted.

On \(|z|=\rho_N\), the elementary inequalities
\(4/N\le|1-Q|\le2\pi/N\), together with \(\rho_N\to1\),
show that the interval for nonzero singular values is
\([cN,CN\log N]\). This statement has no parity or primality
restriction.

## 5. Polylogarithmic conditioning on the full unit disk

The near-unit collar can be transported to unit activity by a stated
physical diagonal gauge, whose cost is polylogarithmic. On the head where
\(L\) acts put
\[
 S_\rho|j\rangle=\rho^{-j}|j\rangle,\qquad
 S_\rho L S_\rho^{-1}=\rho L,\qquad
 \|S_\rho\|\|S_\rho^{-1}\|=\rho^{-d}.
 \tag{21}
\]
Tensor with identities on all other heads. This is only a comparison
of the indicated matrix factors; no source or cap is changed. With
\(\rho=\rho_N\), one has
\(\rho_N^{-d}=(\log N)^{4d/N}\le(\log N)^4\).
Polynomial functional calculus in (21), followed by the inverse bound
of (18), proves the inverse bound below. Its upper bound is even
simpler: (12) gives
\(\sum_{n=1}^{N-1}|r_{N,n}|\le C\log N\), so the triangle
inequality proves it directly on the full unit disk. Thus
\[
 \boxed{\quad
 \|U_N(zL)\|\le C\log N,\qquad
 \|U_N(zL)^{-1}\|\le C(\log N)^4,
 \qquad |z|\le1,\quad N\ge N_0.
 \quad}
 \tag{22}
\]
Thus there is no small physical activity assumption in this estimate.
At \(|z|=1\), equations (10),(19),(22) show that the nonzero
singular values of \(\ell_N(zL)\) lie in
\([cN/(\log N)^4,CN\log N]\). For every compatible left matrix \(B\),
in either the physical operator norm or the Hilbert--Schmidt norm,
\[
 \frac{cN}{(\log N)^4}\|BL\|\le\|B\ell_N(zL)\|
                     \le CN\log N\,\|BL\|,
 \qquad |z|=1,\quad N\ge N_0.
 \tag{23}
\]
Its kernel and image are still exactly (19). The same proof as (20)
applies, now using the bounds of (22). The gauge has not introduced
an unknown metric inverse or an exponential conditioning factor.

## 6. Physical Fourier extraction at unit activity

Let \(\mathsf n\) be the total integer occupation on the remaining
\(r\) heads and \(D_\theta=e^{-i\theta\mathsf n}\). The operators
\(E\) and \(L\) both lower that degree by one. The literal reduced
crossing \(b\) preserves it: each original crossing and every term
of the prefix and its inverse preserve total occupation, and the
first-head zero extraction retains the remaining degree. Therefore
\[
 D_\theta E D_\theta^{-1}=e^{i\theta}E,\qquad
 D_\theta L D_\theta^{-1}=e^{i\theta}L,\qquad
 D_\theta bD_\theta^{-1}=b.
 \tag{24}
\]
All these diagonal matrices are unitary in the original Euclidean
basis. Set \(F(\xi)=\mathcal E_N(\xi E)b\ell_N(a\xi L)\).
Equation (24) gives the exact operator identity
\[
 F(e^{i\theta})=D_\theta F(1)D_\theta^{-1},\qquad
 [\xi^t]F=\mathsf P_tF(1),\quad
 \mathsf P_tB=\frac1{2\pi}\int_0^{2\pi}
             e^{-it\theta}D_\theta BD_\theta^{-1}\,d\theta.
 \tag{25}
\]
The map \(\mathsf P_t\) keeps precisely the entries whose output
degree is the input degree minus \(t\). Its operator norm as a map
on operator norm is at most one, by unitary averaging and the triangle
inequality. In Hilbert--Schmidt norm it is an orthogonal projection:
the different degree differences are disjoint matrix-entry supports.
In particular they obey Parseval on this full matrix space. This
projection is not an assertion about a selected geometric window.

Combining (6),(23),(25) proves the uniform actual Ward estimate
\[
 \boxed{\quad
 \|\mathfrak D_t\|
 \le C m|F_t|N\log N\,
                  \|\mathcal E_N(E)bL\|,
 \qquad 1\le t<N,\quad N\ge N_0,
 \quad}
 \tag{26}
\]
in either of the two stated physical norms. Thus all transfers are
resummed before estimation, and extraction has norm at most one.
The same unit-activity q-log factor estimate (23) permits any left
exterior inside the norm, while the extraction identity (25) is
applied before such an exterior unless it respects the degree action.
The factorial \(F_t\), which can carry exponential size, is explicitly
retained. Terms of \(F\) with degree at least \(N\) can occur; (25)
projects them out for the specified observation and does not replace
the full matrix \(F(1)\) by a low-degree truncation.

The equality (9) keeps the original co-source on this normal insertion.
Its contour can have cancellation, and its arbitrary co-source can
annihilate a nonzero matrix. Consequently (23) does not give a lower
bound after coefficient extraction or for the marked scalar. The
full-activity Euler matrix, the crossing factor and their geometric
contour remain separate analytic objects. The small-activity
factorization [C] and coherent chart [F] are not being extended to
unit activity by (26).

The exact negative-boundary and word cocycle laws of [W, (21)] may
be applied to (6), retaining their actual inverse matrices and every
normal insertion. No bound for those inverses or a general word's
remaining co-source is supplied by (18). All identities are at fixed
quantum root; no quantum-normal derivative or identification of an
off-circle geometric clock with a physical weight is used.

## Complete sources and coverage

* W, complete proof direct: notes/research_actual_word_normal_cocycle_and_source.md,
  458 lines, SHA256
  db453e02bc349e7740b2718b25819e9aa8ad1a71b86044fb7128524bea292106.
* C, complete proof direct: notes/research_root_capped_euler_coproduct_factorization.md,
  360 lines, SHA256
  e11f5f827f226ee93505e00aed3885a33abdbfc15ee71e023a67c048c9c17720.
* F, complete coverage: notes/research_actual_coupled_euler_coherent_flow.md,
  498 lines, SHA256
  a7d3d29f4381f669fd3f6e72a6c637fa259e650757bd39a517e47c0419692def.

All three complete texts were read untruncated in the author sequence.
The finite logarithm itself and small-activity Euler bounds are prior
coverage. The all-transfer Ward coefficient, normalized q-log collar,
accretivity estimate and uniform extraction cost are proved above.
The complete matching final is to receive independent whole-text and
whole-source review. Only written mathematics and text/hash operations
were used; earlier frozen files were not changed.
