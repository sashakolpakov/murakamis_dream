# A positive geometric resolvent probe and its returning source error

21 November 2026. Research note; earlier finals and public manuscripts
remain unchanged.

The actual Newton algebra has positive, source-driven resolvent vectors
at every real spectral parameter below \(-2\). They give explicit
full-dimensional candidates at the crossing-circle trace supplied by
the complete geometry. A turned probe also has a uniformly nonzero
pairing with the original recoupling polynomial.

Those properties do not suffice for scalar transport through short
pieces. We compute the defect for one actual crossing. Its original
marked pairing is zero, but the following inverse crossing makes its
pairing exponentially large. The exact two-crossing word still acts
as the identity. This tests the proposed probe with the original source
retained, rather than with an arbitrary observation.

## 1. The original Newton data and a forced positive vector

Use the full algebra, source and signed crossing polynomials of the
[canonical crossing theorem](research_canonical_crossing_outer_chart_carry.md).
Thus \(N\ge2\), \(d=N-1\), \(q=e^{\pi i/N}\), and
\[
 P_N(X)=2T_N(X/2)+2,\qquad
 c_j=2\cos((2j+1)\pi/N),\qquad
 S_r=\prod_{h=1}^r2\sin(\pi h/N),\quad S_0=1,
\]
\[
 e_r(X)=S_r^{-2}\prod_{j=0}^{r-1}(c_j-X),\qquad
 \mathcal A_N=\mathbb C[X]/(P_N),\qquad
 \phi_N(f)=(-1)^dN^2[X^d]\operatorname{rem}_{P_N}f.
                                                               \tag{1}
\]
The Newton coordinate norm makes the \(e_r\) orthonormal.
The actual unscaled turn satisfies
\[
                   Je_r=e_{d-r},\qquad J^2=I.                  \tag{2}
\]
All value and first-normal data at the double Casimir roots are
included in this \(N\)-dimensional algebra.

Multiplication by \(X\) has the matrix
\[
 Ze_r=c_re_r-\{2\sin(\pi(r+1)/N)\}^2e_{r+1}\quad(r<d),
                         \qquad Ze_d=c_de_d.                  \tag{3}
\]
This follows directly by adding the next Newton factor. In the final
row the next product is a multiple of \(P_N\).
Its diagonal has norm at most two and its weighted shift has norm
at most four; hence \(\|Z\|\le6\).

For a real parameter \(z<-2\), let
\[
 g_{N,z}(X)=
              \frac{1-P_N(X)/P_N(z)}{X-z}.                     \tag{4}
\]
The numerator vanishes at \(X=z\), so (4) is a canonical polynomial
of degree at most \(d\). Its class is \((X-z)^{-1}\). Solving
the triangular equation \((Z-z)g=1\) gives its full Newton vector:
\[
 \boxed{\quad
 g_{N,z}=\sum_{r=0}^d v_r(z)e_r,\qquad
 v_r(z)=\frac{S_r^2}{\prod_{j=0}^r(c_j-z)}>0.
 \quad}                                                        \tag{5}
\]
Indeed the first coefficient is \(1/(c_0-z)\), and every subsequent
coefficient is obtained by multiplying by
\(\{2\sin(\pi r/N)\}^2/(c_r-z)\).
No noninteger Casimir color has been introduced.

For \(z<-6\), the same actual vector has the uniform bound
\[
                   \|g_{N,z}\|\le\frac1{-6-z},\qquad
                   \|Jg_{N,z}\|=\|g_{N,z}\|.                   \tag{6}
\]
For example, \(\|(Z-z)v\|\ge(-z-\|Z\|)\|v\|\) proves the first
inequality, and (2) proves the second. On a compact set of real
parameters below \(-6\) these bounds are independent of \(N\).
On this outer chart,
\(\|(Z-z)g_{N,z}\|/\|g_{N,z}\|\ge-6-z>0\).
The forcing in (5) therefore cannot be dropped to make a homogeneous
approximate eigenvector there. No such assertion is made closer to
the physical interval.

## 2. Pairings with the original mark

For every canonical polynomial \(f\), polynomial division gives
\[
 f\,g_{N,z}=f(z)g_{N,z}+q_{f,z}\quad\text{in }\mathcal A_N,
 \qquad q_{f,z}(X)=\frac{f(X)-f(z)}{X-z}.                       \tag{7}
\]
Here \(\deg q_{f,z}\le N-2\), so \(\phi_N(q_{f,z})=0\).
The leading coefficient in (4) is \(-1/P_N(z)\). Consequently
\[
 \boxed{\quad
 \phi_N(fg_{N,z})=s_N(z)f(z),\qquad
               s_N(z)=\frac{(-1)^NN^2}{P_N(z)}
                         =\phi_N(g_{N,z})>0.
 \quad}                                                        \tag{8}
\]
This is an evaluation represented by an actual source-driven vector.
Its scalar normalization \(s_N\) must be retained.

The actual recoupling polynomial at the original folded label
\(0\le\alpha\le\lfloor d/2\rfloor\) is
\[
                 p_{\alpha,N}(X)
                      =\sum_{j=0}^d e_j(c_\alpha)e_j(X).
                                                               \tag{9}
\]
The exact Newton source identities give
\(\phi_N(p_{\alpha,N}f)=(Jf)(c_\alpha)\).
Therefore the turned positive probe has the particularly simple
marked pairing
\[
 \boxed{\quad
             \phi_N(p_{\alpha,N}Jg_{N,z})
                           =\frac1{c_\alpha-z}>0 .
 \quad}                                                        \tag{10}
\]
Uniformly in the level and folded label,
\[
          \frac1{2-z}\le\frac1{c_\alpha-z}\le\frac1{-2-z}.
                                                               \tag{11}
\]
Thus this original pairing has zero exponential rate, even though
it is nonzero and well controlled. The unturned pairing is instead
\[
             \phi_N(p_{\alpha,N}g_{N,z})
                           =s_N(z)p_{\alpha,N}(z)>0.            \tag{12}
\]
Positivity in (12) follows directly from (9): at \(z<-2\) every
\(e_j(z)\) is positive, and \(e_j(c_\alpha)\) is nonnegative
for \(j\le\alpha\) and zero for \(j>\alpha\). Neither (10) nor
(12) identifies an arbitrary short exterior with this probe.

In the actual complete crossing-circle geometry the target is
\(z=2-4/c^2\), with the prescribed rectangle ratio \(c>0\).
For \(0<c<1/\sqrt2\) it belongs to the outer region \(z<-6\)
of (6). Equations (5), (8) and (10) therefore give full actual
vectors and marked pairings at those geometric parameters.
They do not assign their pairings the hyperbolic volume.

## 3. A source-null crossing defect returns after the inverse crossing

Write \(R_N^+\) and \(R_N^-\) for the original canonical signed
crossing polynomials. They are inverses in the full physical algebra:
\[
                              R_N^-R_N^+=1.
 \]
For the positive crossing define the actual defect
\[
           q_{N,z}(X)=\frac{R_N^+(X)-R_N^+(z)}{X-z}.            \tag{13}
\]
It has degree at most \(N-2\). Equation (7) says
\[
 R_N^+g_{N,z}=R_N^+(z)g_{N,z}+q_{N,z},\qquad
                              \phi_N(q_{N,z})=0.              \tag{14}
\]
Apply the actual inverse crossing and then the same original mark.
Using (8) gives the exact identity
\[
 \boxed{\quad
 \phi_N(R_N^-q_{N,z})
        =\{1-R_N^+(z)R_N^-(z)\}\,s_N(z).
 \quad}                                                        \tag{15}
\]
In terms of the exact inverse-word carry
\[
                 C_N(z)=\frac{R_N^+(z)R_N^-(z)-1}{P_N(z)}
 \]
already retained in the canonical crossing theorem, this is
\[
                     \phi_N(R_N^-q_{N,z})
                              =(-1)^{N+1}N^2C_N(z).           \tag{16}
\]
On compact real subsets of \(z<-6\), the proved outer carry estimate
therefore yields
\[
 \boxed{\quad
 \phi_N(R_N^-q_{N,z})
    =\frac{(-1)^{N+1}P_N(z)}
                 {N^2(z-c_0)^2}(1+O(N^{-2})).
 \quad}                                                        \tag{17}
\]
The factor \(N^2\) in (16) is important: the leading denominator
in (17) is \(N^2\), not \(N^4\).

Let \(w+w^{-1}=z\) with \(|w|>1\). Since
\(P_N(z)=w^N(1+w^{-N})^2\), (8) and (17) give
\[
 \frac1N\log s_N(z)\longrightarrow-\log|w|,\qquad
 \frac1N\log|\phi_N(R_N^-q_{N,z})|
                                  \longrightarrow\log|w|>0.  \tag{18}
\]
The initially source-null correction has become exponentially
visible after one fixed adjacent inverse crossing. In the exact
word it cancels the large value
\(R_N^+(z)R_N^-(z)s_N(z)\), leaving precisely \(s_N(z)\).
All these assertions concern a literal crossing followed by its
inverse, at every level parity, with its original unit phases.

## 4. Consequence for the geometric candidate

The positive inhomogeneous probe (5) respects the full boundary
algebra and prescribed marked source. It is a legitimate candidate
to test in a geometric construction. Its original pairings are
explicit, and its norm is bounded on the stated outer chart.

The calculation (13)--(18) rules out one proposed simplification
for that candidate: a direction invisible to the present mark
cannot be removed before arbitrary fixed short transport. A lower
certificate would have to retain this defect, or prove its coherent
cancellation in the actual whole boundary field. The identities
do not rule out other source-driven packets, semidefinite force
certificates, or a successful complete-period argument.

## Proof source and coverage

The complete matching proof source was read:

| Source | SHA-256 |
|---|---|
| [Canonical crossing and retained carry](research_canonical_crossing_outer_chart_carry.md) | f26d45f356e1efeb209bf59a556c1ce17eb54aca4e170d3e02b4b38fa50945be |

For coverage, the inverse entries in (5) are already in
[the original resolvent-rate note](research_original_casimir_resolvent_rate.md),
Section 1. The full Newton reproducing kernel behind (8)--(12) is
already in [the polarization note](research_diagonal_flip_quantum_polarization.md),
Section 7. Both complete texts were read for this comparison.
No novelty is claimed for these resolvent or reproducing identities.
They are derived above from the actual Newton data; none of the
broader asymptotic assertions in those notes is an assumption here.
The additional diagnostic is the actual marked return calculation
(15)--(18).

Only written mathematics and text/hash operations were used. No
mathematical program, test, numerical experiment, build, git operation
or earlier-final edit was performed.
