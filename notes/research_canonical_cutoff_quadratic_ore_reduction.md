# A quadratic equation for the actual canonical cutoff source

Private written proof, 18 November 2026.

The cutoff source of [C] has a uniform exponential type on a meridian
disk whose radius is much larger than that type. This permits removal
of the complementary factor of the actual quantum operator by analytic
estimates. The resulting monic quadratic quasiequation retains the
same canonical source and its endpoint error. No ordering of the other
characteristic moduli is required.

This is not yet transport of the nonzero node coefficient to a fixed
meridian. It supplies the two-branch equation needed for that next step.

## 1. Actual source and assertion

Use the source, operator, and transverse simple-node hypotheses of [C].
Thus the original finite-shift operator is
\[
 \mathcal P_h=\sum_{\nu\in J}p_\nu(h,Y)T^\nu,
 \qquad Tf(Y)=f(e^hY),\qquad h=\log Q,
 \tag{1}
\]
with holomorphic coefficients near \((0,\alpha)\), where
\(\alpha\ne0,1\). Its classical symbol satisfies
\[
 P(Y,1)\equiv0,\quad P_L(\alpha,1)=0,\quad
 P_{LL}(\alpha,1)P_{YL}(\alpha,1)\ne0.
 \tag{2}
\]
The two canonical cutoff functions of [C] have a fixed small endpoint
\(R\ne0\) and satisfy the original exact equation
\[
 \mathcal P_h U_{R,\pm}=e^{-R/h}J_{R,\pm},
 \tag{3}
\]
where the currents extend jointly holomorphically through
\((h,Y)=(0,\alpha)\), on disks chosen after \(R\). Their difference
obeys the same identity with the difference of the currents.
All cut, framing, and normal conventions are those of [C].

Put \(x=\log(Y/\alpha)\), with \(x=0\) at the node. Then
\(T f(x)=f(x+h)\). Let \(\ell(x)\) denote the other local classical
root through \(1\), so \(\ell(0)=1\). Conditions (2) and division
by \(L-1\) give this holomorphic root by the implicit function
theorem; its derivative at zero is nonzero.

**Theorem.** There is a sufficiently small fixed cutoff \(R\) and
a disk \(|x|<\delta\), with \(\delta=c_0\sqrt{|R|}\), on which
the following holds for all sufficiently small nonzero complex \(h\).
There is one monic quadratic operator
\[
 \mathcal S_h=T^2+s_{1,h}(x)T+s_{0,h}(x),\qquad
 \mathcal S_0=T^2-(1+\ell(x))T+\ell(x),
 \tag{4}
\]
constructed only from (1), such that its coefficients are holomorphic
in \(x\), uniformly bounded, and
\[
             \|s_{j,h}-s_{j,0}\|\le C|h|.
 \tag{5}
\]
For either canonical cutoff and their difference, on a smaller fixed
disk and every closed sector facing \(R\),
\[
                    \|\mathcal S_h U\|
                         \le C_R e^{-\Re(R/h)}.
 \tag{6}
\]
Every fixed meridian derivative has the analogous bound on smaller
disks. No inversion of an unknown source scalar is used.

The finite truncation depth used below depends on \(|h|\). We assert
holomorphy of the constructed coefficients in \(x\), not their joint
holomorphy at \(h=0\). Equation (6) is an estimate for the actual
cutoff functions, not an exact homogeneous equation or a replacement
of them by newly chosen solutions.

## 2. The actual source has type proportional to the cutoff

We need the constants in the type estimate before choosing \(R\).
The Laurent coefficients in [C], equation (5), have a fixed bound
\(CD^k\), independent of \(R\). In its primitive formula choose
\(|z|\le c\sqrt{|R|}\), where \(z=Y-\alpha\), with a fixed sufficiently
small \(c\). Then, for both endpoint roots,
\[
 |w_{R,\pm}|^2\asymp |R|,\qquad |z/w_{R,\pm}|\le c_1<1,
 \tag{7}
\]
with constants independent of sufficiently small \(R\).
The three arguments of the convergent function \(H\) in [C] remain
in a fixed smaller polydisk. The denominators of the integrated
Laurent monomials have modulus at least one. The binomial coefficients
of the primitive kernel sum to \(2^{a-1}\).

More explicitly, the endpoint terms in [C], equation (8), are a
bounded convergent coefficient sum times \(w^{2a-1}\). The terms
at the initial endpoint have the same bound: factor out
\(w^{2a-1}(z/w)\), and use \(|z/w|^{2l}\le1\). The remaining
coefficient series converge uniformly as \(R\to0\). Thus constants
\(C,C_1\), independent of small \(R\) and of \(a\), give
\[
 |I^a\mathcal B(z,R)|
       \le C C_1^a\frac{|R|^{a-1/2}}{(a-1)!}.
 \tag{8}
\]
The exact endpoint expansion of the cutoff consequently yields
\[
 \|U_{R,\pm}(h,\cdot)\|
 \le C\frac{\sqrt{|R|}}{|h|}
                \exp\!\left(\frac{C_2|R|}{|h|}\right)
 \tag{9}
\]
on a disk of radius a fixed multiple of \(\sqrt{|R|}\), for all
\(h\ne0\). We used \(|e^{-R/h}|\le e^{|R|/|h|}\); hence this
bound does not require a facing sector. The difference of the two
cutoffs satisfies the same bound after increasing \(C\).

The logarithmic coordinate is uniformly comparable to \(z\) near
zero. Choose \(c_0>0\) small enough that (9) holds on
\(|x|<8\delta\), \(\delta=c_0\sqrt{|R|}\). All constants in
(9), including its type \(C_2|R|\), are chosen before \(R\).
The bounded-current constant in (3) may depend on the subsequently
fixed \(R\); it is independent of \(h\).
The Cauchy construction of that current in [C] can use a circle at
any fixed smaller fraction of this source disk. After decreasing
\(c_0\) if necessary, (3) and a bounded current therefore hold on
\(|x|<6\delta\), with an \(h\)-radius chosen after \(R\). Indeed the
local endpoint-sheet currents cover that circle, and its finite
subcover gives a common \(h\)-radius before Cauchy extension inside.
No uniform lower bound for this \(h\)-radius as \(R\to0\) is needed.

## 3. Analytic factorization of the actual shift operator

Choose a fixed integer \(a\ge0\) so that
\(\widehat{\mathcal P}_h=T^a\mathcal P_h\) is a polynomial in \(T\).
Its coefficients are the actual shifted functions
\(p_\nu(h,x+ah)\). Its source equation is exactly
\[
 \widehat{\mathcal P}_h U=e^{-R/h}\widehat J_R,
 \qquad \widehat J_R(h,x)=J_R(h,x+ah).
 \tag{10}
\]
The endpoint is fixed in the meridian, so this shift creates no
additional exponential factor.

Let \(d\ge2\) be its fixed polynomial degree, allowing vanishing
top coefficients at \(h=0\). The classical factorization is
\[
 \widehat P_0(x,L)=Q_0(x,L)S_0(x,L),\qquad
 S_0=(L-1)(L-\ell(x)),\qquad \deg Q_0\le d-2.
 \tag{11}
\]
Here \(Q_0(0,1)\ne0\). Shrink one original node chart so that
\(Q_0\) and \(S_0\) are coprime throughout it, and
\(|Q_0(x,1)|\ge c>0\). This uses only (2), not simplicity or
nonvanishing of the other roots.

The coefficient map
\[
 (q,s)\longmapsto qS_0+Q_0s,
 \qquad \deg q\le d-2,\quad \deg s\le1,
 \tag{12}
\]
is invertible, with holomorphic uniformly bounded inverse on that
chart. Indeed, reduction modulo the monic quadratic \(S_0\)
makes multiplication by \(Q_0\) invertible in its two-dimensional
quotient. This determines \(s\); monic polynomial division then
determines \(q\). This argument does not divide by the leading
coefficient of \(Q_0\). It also proves uniform invertibility for
all sufficiently small coefficient perturbations of \(Q_0,S_0\),
with the quadratic factor kept monic.

For left-ordered shift polynomials, the actual product is
\[
 (Q\# S)(x,T)=\sum_{i,j}q_i(x)s_j(x+ih)T^{i+j}.
 \tag{13}
\]
We construct \(Q_h,S_h\) with this product. Start with \(Q_0,S_0\).
Their residual from \(\widehat{\mathcal P}_h\) is \(O(|h|)\)
on a fixed smaller original chart, since the actual coefficients
are holomorphic in \(h\) and the original classical factors have
bounded derivatives there.

Suppose a current residual has norm \(\varepsilon\), and the
factors are \(O(|h|)\) from their classical values. Solve, pointwise,
\[
                  qS+Qs=\widehat P_h-Q\# S
 \tag{14}
\]
using (12) for the current factors. The correction has norm
\(\|q\|+\|s\|\le C\varepsilon\), and \(\deg s\le1\), preserving
monicity. On a disk eroded by \(\sigma\ge2d|h|\), replace the
factors by \(Q+q,S+s\). Cauchy's estimate in (13) gives
\[
 \varepsilon_{\rm new}
       \le C\left(\frac{|h|}{\sigma}\varepsilon+\varepsilon^2\right).
 \tag{15}
\]
To verify it, subtract (14) from the actual product expansion.
The two linear differences are
\(q\# S-qS\) and \(Q\# s-Qs\). Their shifted coefficient
differences cost at most \(C|h|/\sigma\) times the correction
norm. The remaining term \(q\# s\) is quadratic. All shift
lengths are bounded by \(d|h|\).

Take \(m=\lfloor c\delta/|h|\rfloor\) iterations, with a total
erosion at most \(\delta\). Choose the fixed \(c>0\) sufficiently
small that \(\sigma=\delta/m\) makes the linear contraction in
(15) at most \(1/4\) and keeps all shifts legitimate. For small
\(|h|\), the quadratic term costs at most another \(1/4\).
The residuals decrease by a factor at least \(1/2\), and their
corrections sum to \(O(|h|)\); this verifies the maintained
coprimality and boundedness. Reserve further fixed buffers for
the finitely shifted evaluations. On \(|x|<6\delta\) the resulting
factors are holomorphic and bounded, satisfy (5), and on
\(|x|<5\delta\) obey
\[
 \widehat{\mathcal P}_h=Q_h\#\mathcal S_h+E_h,
 \qquad \|E_h\|\le C e^{-c_2\delta/|h|}.
 \tag{16}
\]
Here and below a norm of a shift polynomial is the sum of its
coefficient sup norms. The harmless initial factor \(|h|\) was
dropped. All constants in this construction are uniform for small
\(\delta\), because its coefficient and inverse bounds came from
one fixed original node chart.

## 4. Removing the complementary factor on the actual source

Put \(f=\mathcal S_hU\). Its outer norm, on \(|x|<4\delta\), is
bounded by a fixed multiple of the source norm (9), with all finite
shifts still inside the source disk. By (10) and (16),
\[
          Q_h f=e^{-R/h}\widehat J_R-E_hU.
 \tag{17}
\]
The second term is bounded by the coefficient norm of \(E_h\)
times the same outer source bound.

Write \(Q_h=\sum_iq_{i,h}(x)T^i\), and set
\[
 a_h(x)=\sum_iq_{i,h}(x),\qquad
 K_hg=-a_h^{-1}\sum_iq_{i,h}(x)(T^i-1)g.
 \tag{18}
\]
Since \(a_h=Q_0(x,1)+O(h)\), its inverse is uniformly bounded.
For a holomorphic function on a disk, with its target disk eroded
by \(\sigma\ge2d|h|\),
\[
                   \|K_hg\|\le C\frac{|h|}{\sigma}\|g\|.
 \tag{19}
\]
This follows by integrating its derivative along the short shifts
and applying Cauchy's estimate. It is an analytic estimate, not a
spectral modulus estimate for \(Q_h\).

If \(Q_h f=g\), the exact identity is
\[
 f=K_h^m f+\sum_{j=0}^{m-1}K_h^j(a_h^{-1}g).
 \tag{20}
\]
Choose another \(m=\lfloor c_3\delta/|h|\rfloor\), eroding at
most \(\delta\) from \(|x|<4\delta\). Choose \(c_3\) so that
each use of (19) has norm at most \(1/2\). The same finite sequence
of nested disks estimates every term of (20). It yields
\[
 \|f\|_{|x|<3\delta}
 \le C e^{-c_4\delta/|h|}\|f\|_{|x|<4\delta}
                     +C\|g\|_{|x|<4\delta}.
 \tag{21}
\]
In particular the actual analytic function \(f\), including any
complementary homogeneous component, is estimated here. No initial
projection onto a preferred subspace is imposed.

Combining (9), (16), (17), and (21), with \(c_5>0\) fixed, gives
\[
 \|\mathcal S_hU\|_{|x|<3\delta}
 \le C_R e^{-\Re(R/h)}+
 C\frac{\sqrt{|R|}}{|h|}
       \exp\!\left[-\frac{c_5\delta-C_2|R|}{|h|}\right].
 \tag{22}
\]
This is the source-specific comparison that pays the elimination.
Because \(\delta=c_0\sqrt{|R|}\), choose the fixed cutoff small
enough that \(c_5\delta-C_2|R|>3|R|\). For this fixed \(R\),
the second term is bounded by a constant times
\(e^{-2|R|/|h|}\) for sufficiently small \(h\). Since
\(\Re(R/h)\le |R|/|h|\), it is smaller than the first displayed
exponential scale. This proves (6). Reserved disk buffers and
Cauchy's formula give the derivative assertions.

## 5. What has been reduced

The same constructed quadratic operator works for both actual
canonical endpoint sheets and their difference. Its principal roots
are exactly the two roots through the Alexander node. The proof
allows repeated complementary roots, roots on either side of the
unit circle, and vanishing extreme coefficients of the original
operator. Only separation of the two-root factor from its complement
near the node was used, and this follows from (2).

The endpoint forcing remains at its original scale in (6). The
canonical source was never replaced by an arbitrarily initialized
quadratic solution. The actual nonzero node profile and shrinking
overlap from [C] therefore accompany this quadratic quasiequation.

This does not yet estimate the two-branch propagation from that
overlap to a fixed nonzero meridian. In particular it does not give
a global analytic factorization, an exact invariant subspace, a
fixed-meridian nonzero coefficient, or identification with the
original finite-color invariant. No classical character-component
or volume identification is made.

Analytic factor iteration and eroded-domain estimates have antecedents
in the repository's regular transport arguments. The addition here
is their explicit application to the actual regularized cutoff,
including the uniform type-versus-radius comparison (22). It does
not assume the end-regularity of a minimal quantum operator.

## 6. Complete proof source

| Label | Complete source | SHA256 |
|---|---|---|
| C | notes/research_canonical_cutoff_node_regularization_and_profile.md | 8c28a3d3a7b11085c8e2b5966221501b632ea99600aae4db57e8bdf8cd4a9631 |

C supplies the actual node source, its convergent Laurent coefficients,
primitive formula, canonical cutoff, and exact endpoint current.
The uniform cutoff type, coefficient factorization, analytic inverse,
and their combined estimate are proved above. Only written mathematics
and source-text reads were used. No mathematical programs, tests,
numerical calculations, or builds were run. Frozen notes and public
manuscripts remain unchanged.
