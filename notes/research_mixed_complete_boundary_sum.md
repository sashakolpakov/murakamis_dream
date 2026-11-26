# Complete boundary weights for mixed three- and four-crossing words

Research proof, 4 November 2026. Frozen manuscripts are unchanged.

The original complete boundary vectors also admit a positive-weight
expansion in the exact contracted basis. This gives a finite quadratic
exponential sum for every mixed word, including all fixed ordinary
boundary derivatives. The weights are nonnegative; their sum still
has an oscillatory phase. We also give an explicit global absolute
variational bound and a strictly concave reduction of its regular
boundary factors. Neither statement supplies a lower bound for the
original mixed-word source.

## 1. The original complete boundary vectors

Use the notation of the
[exact mixed Fourier contraction](research_mixed_wire_exact_contraction.md):
\[
 q=e^{\pi i/N},\quad Q=q^2,\quad D=N-1,\quad
 P_j=(Q^{-1};Q^{-1})_j=\delta_j S_j,
 \qquad S_j=\prod_{a=1}^j2\sin(\pi a/N),
\]
\[
 \delta_j=e^{i\vartheta_N(j)},\qquad
 \vartheta_N(j)=\frac{\pi}{2N}(Dj-j^2),\qquad
 \kappa=q^{D^2/2}.
 \tag{1}
\]
The original Newton basis and evaluation vector are
\[
 c_a=2\cos\frac{(2a+1)\pi}{N},\qquad
 e_l(w)=\frac{\prod_{a=0}^{l-1}(c_a-w)}{S_l^2},
 \qquad v(w)=(e_0(w),\ldots,e_D(w))^T.
 \tag{2}
\]
In particular the complete ordinary color is \(w=-2\). The crossing
matrix is the full repeated-root multiplication matrix; no value-only
quotient is used.

**Lemma 1.** Let \(S\) denote the matrix in equation (13) of the exact
contraction note, and put \(b(w)=Sv(w)\). Then
\[
 S_{jl}=\frac{\delta_j^{-1}q^{jl}}{S_lS_{j-l}}
 \quad(0\le l\le j<N),\qquad S_{jl}=0\quad(l>j),
\]
\[
 b_j^{(k)}(-2)=(-1)^k\delta_j^{-1}
       \sum_{l=0}^j q^{jl}\frac{E_{l,k}}{S_lS_{j-l}},
 \qquad E_{l,k}=(-1)^k e_l^{(k)}(-2)\ge0.
 \tag{3}
\]
These are exact identities at both parities and every derivative order.

*Proof.* The literal crossing coefficients give
\[
 M_{jl}=\kappa(-1)^j q^{j(l+1)}\frac{S_j}{S_lS_{j-l}}.
\]
Multiplying by the diagonal factor
\(\kappa^{-1}(-q)^{-j}/P_j\) proves the first identity. Expand the
product (2) at \(w=-2\). Every \(c_a+2\) is nonnegative, so its
coefficient of \((w+2)^k\), multiplied by \((-1)^k\), is
nonnegative. This proves (3), including the zero factors at odd levels.
It also proves the assertion for the physical repeated-root normals;
no division by \(e_l(-2)\) is involved. \(\square\)

## 2. The full scalar quadratic sum

Fix a word \(n_1,\ldots,n_m\in\{3,4\}\), put
\(\epsilon_v=1_{\{n_v=4\}}\), and \(k_4=\sum_v\epsilon_v\).
For each vertex use two leg indices \(i_v,j_v\). The support is
\[
 i_v,j_v\ge0,\quad i_v+j_v<N,\qquad
 j_v+i_{v+1}<N\ (v<m),\qquad
 0\le l_L\le i_1,\quad0\le l_R\le j_m.
 \tag{4}
\]
Write \(e_L=i_1,e_R=j_m\), and define the nonnegative weight
\[
 \begin{split}
 W_{\mathbf i,\mathbf j,l_L,l_R}^{a,b}
 ={}&\prod_{v=1}^m
       \frac{S_{i_v+j_v}}{(S_{i_v}S_{j_v})^{\epsilon_v}}
       \prod_{v=1}^{m-1}
       \frac{S_{j_v+i_{v+1}}}{S_{j_v}^2S_{i_{v+1}}^2}\\
 &\quad\times
       \frac{E_{l_L,a}}{S_{l_L}S_{i_1-l_L}}
       \frac{E_{l_R,b}}{S_{l_R}S_{j_m-l_R}}.
 \end{split}
 \tag{5}
\]
Here an empty product is one. The exact real phase is
\[
 \begin{split}
 \Theta_N={}&\frac\pi N\left(
       \sum_{v<m}j_vi_{v+1}-\sum_vi_vj_v
                      +i_1l_L+j_ml_R\right)\\
 &+\frac\pi{2N}\sum_v\epsilon_v
                \left(i_v^2+j_v^2-D(i_v+j_v)\right).
 \end{split}
 \tag{6}
\]

**Theorem 2.** With the original matrices \(A_n=JM^n\),
\[
 \left.\partial_{w_L}^a\partial_{w_R}^b
   \bigl[v(w_L)^TA_{n_1}\cdots A_{n_m}v(w_R)\bigr]
                  \right|_{w_L=w_R=-2}
 =(-1)^{a+b}\kappa^{m+k_4}N^{k_4}
       \sum_{(4)}e^{i\Theta_N}W^{a,b}.
 \tag{7}
\]
In particular the same phase works for all fixed ordinary jets. This
is the full undeleted original source, at every level.

*Proof.* Substitute (3) in the all-level identity
\(v_L^TA_{n_1}\cdots A_{n_m}v_R
 =b_L^TB_{n_1}\Gamma\cdots\Gamma B_{n_m}b_R\).
The positive parts of \(B_3,B_4,\Gamma\) give (5). Before inserting
the two boundary vectors, the open-word phase equals
\[
 \vartheta_N(i_1)+\vartheta_N(j_m)
 +\frac\pi N\left(\sum_{v<m}j_vi_{v+1}-\sum_vi_vj_v\right)
 -\sum_v\epsilon_v\{\vartheta_N(i_v)+\vartheta_N(j_v)\}.
 \tag{8}
\]
This follows by expanding
\(\vartheta_N(i+j)=\vartheta_N(i)+\vartheta_N(j)-\pi ij/N\).
The factors \(\delta_{i_1}^{-1},\delta_{j_m}^{-1}\) in (3)
cancel precisely the first two terms of (8), while \(q^{i_1l_L+j_ml_R}\)
adds the endpoint cross terms in (6). Each three-crossing vertex
contributes \(\kappa\); each four-crossing vertex contributes
\(\kappa^2N\). This proves the scalar and every sign in (7).
\(\square\)

The nonnegative weights in (7) are not a positive measure whose total
is the original source: \(e^{i\Theta_N}\) remains inside the sum.
The formula does not identify arbitrary words or closures with knots.

## 3. A global absolute variational bound

For real \(0\le u\le1\) define continuous primitives
\[
 J(u)=\int_0^u\log(2\sin\pi r)\,dr,\qquad
 \mathcal V(u)=2\int_0^u\log(2|\cos\pi r|)\,dr-2J(u).
 \tag{9}
\]
The integrable singularities in these formulas have their usual limits.
On \(0\le u\le1/2\),
\(\mathcal V(u)=V_0(u)=-2J(1/2-u)-2J(u)\).
For each fixed \(k\), uniformly in all physical indices,
\[
 S_j=\exp\{NJ(j/N)+O(\log N)\},\qquad
 0\le E_{l,k}\le N^{C_k}e^{N\mathcal V(l/N)}.
 \tag{10}
\]
The upper bound includes the odd zero and its nonzero normals.

For clarity, (10) needs no uniform smoothness at a sine zero. Split the
Riemann sum into monotone pieces on either side of each sine or cosine
zero. On each piece the integral comparison error is bounded by its
endpoint logarithms, hence \(O(\log N)\). The cosine product in (2)
samples \(4\cos^2(\pi(a+1/2)/N)\). Every nonzero factor is bounded
below by a fixed power of \(N^{-1}\). At odd levels there is just one
exact zero; a nonzero differentiated product must remove it. Removing
at most \(k\) factors and summing at most \(N^k\) terms changes
only the polynomial factor. This proves the second estimate.

There is also a sharp regular **real-index** symbol. For each fixed
\(k\), uniformly when \(u=l/N\) stays in a compact subinterval of
\((0,1/2)\),
\[
 E_{l,k}=N^{k-1}\frac{1}{2\sin\pi u}
       \left(\frac{\tan\pi u}{4\pi}\right)^k
       e^{NV_0(u)}\bigl(1+O(N^{-1})\bigr).
 \tag{10a}
\]
Indeed the midpoint cosine product has no order-one endpoint factor,
whereas \(S_l^2=2N\sin(\pi u)e^{2NJ(u)}(1+O(N^{-1}))\).
For the derivatives, put \(r_a=(c_a+2)^{-1}\). The product rule gives
\(E_{l,k}=e_l(-2)k!\,\mathrm e_k(r_0,\ldots,r_{l-1})\), and
midpoint summation gives
\[
 \sum_{a<l}r_a=\frac{N\tan\pi u}{4\pi}+O(N^{-1}),\qquad
 k!\,\mathrm e_k(r_a)=\left(\sum_{a<l}r_a\right)^k
                       (1+O(N^{-1})).
\]
The second estimate follows by bounding the repeated-index terms in
the power expansion; each \(r_a\) is bounded on this compact set.
The coefficient in (10a) is nonzero there. This real-index statement
does not assert a uniform complex interpolation of the original
products; such interpolation is a separate requirement for a saddle
deformation.

Let \(s_v=i_v/N,t_v=j_v/N,u_L=l_L/N,u_R=l_R/N\).
Denote the closed polytope obtained from (4), with \(<N\) replaced
by \(\le1\) after scaling, by \(\mathcal P_m\). Its entropy is
\[
 \begin{split}
 \mathcal H={}&\sum_v\bigl[J(s_v+t_v)
                     -\epsilon_v(J(s_v)+J(t_v))\bigr]\\
 &+\sum_{v<m}\bigl[J(t_v+s_{v+1})-2J(t_v)-2J(s_{v+1})\bigr]\\
 &+\sum_{(e,u)=(s_1,u_L),(t_m,u_R)}
                [\mathcal V(u)-J(u)-J(e-u)].
 \end{split}
 \tag{11}
\]
Thus the literal complete source and every fixed ordinary jet obey
\[
 |\partial_L^a\partial_R^b\mathcal Z_N(-2,-2)|
       \le N^{C_{m,a,b}}\exp\{N\max_{\mathcal P_m}\mathcal H\}.
 \tag{12}
\]
This is a finite-dimensional global upper reduction: all endpoint
indices, including the high sector, remain in \(\mathcal P_m\).
It follows directly from (5), (10), and the at most \(N^{2m+2}\)
terms in (7). It does not assert that this absolute maximum equals the
original geometric action.

## 4. Exact optimization of a regular complete endpoint

**Proposition 3.** For \(0<e<1/2\), put
\[
 B(e,u)=V_0(u)-J(u)-J(e-u),\qquad0<u<e.
 \tag{13}
\]
The function \(B\) is strictly jointly concave. For each fixed \(e\)
it has a unique global maximum \(u(e)\) on \([0,e]\). It lies in
\((0,e)\), and is given by the unique positive root
\[
 z^3\sec(\pi e)+z=\tan(\pi e),\qquad
                 u(e)=\pi^{-1}\arctan z.
 \tag{14}
\]
The optimized boundary value \(\widehat B(e)=B(e,u(e))\) is
strictly concave.

*Proof.* Direct differentiation gives
\[
 B_u=\log\frac{\cos^2(\pi u)\sin(\pi(e-u))}{\sin^3(\pi u)},
 \qquad B_e=-\log(2\sin\pi(e-u)),
\]
\[
 -d^2B=
 \pi[2\tan(\pi u)+3\cot(\pi u)]\,du^2
                 +\pi\cot(\pi(e-u))(de-du)^2.
 \tag{15}
\]
Both coefficients are positive. Also \(B_u\to+\infty\) at
\(u=0\) and \(B_u\to-\infty\) at \(u=e\). Hence the unique
critical point is the global maximum, including both endpoints.
Writing \(z=\tan\pi u\), \(w=\tan\pi e\), its equation becomes
\((w-z)/(z^3\sqrt{1+w^2})=1\), giving (14). The left side
of (14) is strictly increasing in \(z\), with its root in \((0,w)\).
Finally, if \(a=\pi(2\tan\pi u+3\cot\pi u)\) and
\(b=\pi\cot\pi(e-u)\), the optimized second derivative is
\[
                         \widehat B''(e)=-\frac{ab}{a+b}<0.
 \tag{16}
\]
This is the exact Schur complement of (15). \(\square\)

## 5. The actual complex complete-end critical point

The maximizer in Proposition 3 concerns absolute weights. The source
phase also contains the endpoint Fourier term in (6), so its boundary
stationarity equation is instead
\(B_u(e,u)+i\pi e=0\).

**Proposition 4.** For every real \(0<e<1/2\), this equation has
exactly one solution in \(0<\Re u<e\). It is simple and satisfies
\[
 z=\tan(\pi u)=\frac{i+\sqrt{1-2X}}2,
 \qquad X=e^{2\pi i e},\qquad
 0<\Re u<\min(e,1/4),\quad\Im u>0.
 \tag{17}
\]
The square root has positive real and negative imaginary parts. The
arctangent is continued from \(e\downarrow0\). The solution extends
holomorphically to a neighborhood of every compact real interval
\(e\in(0,1/2)\).

*Proof.* Exponentiating the stationarity equation and using (15) gives
\[
 2z^3+(X+1)z+i(X-1)
            =(z+i)(2z^2-2iz+X-1)=0.
 \tag{18}
\]
The value \(-i\) is never attained by the tangent of a finite complex
number. Write the square root in (17) as \(A-iB\). For
\(\alpha=2\pi e\in(0,\pi)\), its defining number has negative
imaginary part, so \(A,B>0\). Moreover
\[
 B^2=\frac{\sqrt{5-4\cos\alpha}-1+2\cos\alpha}{2}<1,
\]
because
\((3-2\cos\alpha)^2-(5-4\cos\alpha)=4(1-\cos\alpha)^2>0\).
Thus the selected root \(z=a+ib\) has \(a>0\) and \(0<b<1/2\).
The other quadratic root has negative real part, so cannot be the
tangent of a point in \(0<\Re u<e<1/2\).

The equation \(|X|=1\), with \(X=1+2iz-2z^2\), gives
\[
 a^2=b(1-b)+\sqrt{b(1-b)},\qquad
 |z|^2=b+\sqrt{b(1-b)}<1.
 \tag{19}
\]
Consequently \(R=(1+iz)/(1-iz)=e^{2\pi i u}\) has modulus
less than one and argument in \((0,\pi/2)\). This proves
\(\Im u>0\) and \(0<\Re u<1/4\). It remains to check
\(\Re u<e\) when \(e<1/4\). Both \(R\) and \(X\) then
have positive real part, and
\[
 (1-2b)(1-a^2-b^2)-\Re X
 =a^2(1+2b)-b^2(3-2b)
 =b(1-2b)+(1+2b)\sqrt{b(1-b)}>0.
 \tag{20}
\]
Since \(\Im X=2a(1-2b)\) and
\(\tan\arg R=2a/(1-|z|^2)\), (20) gives
\(\arg R<\arg X\), as required.

The chosen logarithms therefore continue inside the original regular
strip throughout this interval. The exponentiated equation can differ
from the asserted logarithmic equation only by a constant multiple of
\(2\pi i\). Its small-\(e\) expansion is
\(u=e-\pi^2e^3+O(e^4)\), which gives \(B_u+i\pi e\to0\)
in those branches. Hence that multiple is zero. Finally the quadratic
derivative is \(4z-2i=2\sqrt{1-2X}\ne0\), so the root is simple
and has the stated holomorphic continuation. \(\square\)

This determines the original endpoint stationary equation, including
its log lift. It does not establish a deformation of its full finite
sum to that critical point.

## 6. The open-word regular phase and the remaining contour problem

On the connected regular complex chamber
\[
 \begin{gathered}
 0<\Re s_v,\Re t_v<1/2,\qquad
 1/2<\Re(s_v+t_v)<1,\quad
 1/2<\Re(t_v+s_{v+1})<1,\\
 0<\Re u_L<\Re s_1<1/2,\qquad
 0<\Re u_R<\Re t_m<1/2,
 \end{gathered}
 \tag{21}
\]
continue the original logarithms from the real chamber. The leading
holomorphic phase of the scalar terms is
\[
 \mathcal F=\mathcal H+i\pi\left[
    \sum_{v<m}t_vs_{v+1}-\sum_vs_vt_v+s_1u_L+t_mu_R
       +\frac12\sum_v\epsilon_v(s_v^2+t_v^2-s_v-t_v)\right],
 \tag{22}
\]
where (11) uses the holomorphic \(V_0\) at both ends. The finite
correction from \(D=N-1\) is the explicit amplitude phase
\(\exp[\frac{\pi i}{2}\sum_v\epsilon_v(s_v+t_v)]\).
There is no missing endpoint linear phase.

For real horizontal differentials, the quadratic oscillation in (22)
has purely imaginary Hessian. The negative real Hessian of (22) is
therefore the sum of these positive forms:

* each vertex or shared sum \(z=l_1+l_2\) contributes
  \(-\pi\Re\cot(\pi z)(dl_1+dl_2)^2\);
* an internal leg at vertex \(v\) contributes
  \((2+\epsilon_v)\pi\Re\cot(\pi l)\,dl^2\), and an endpoint
  leg contributes \(\epsilon_v\pi\Re\cot(\pi l)\,dl^2\);
* each complete end contributes the real part of (15).

For \(0<\Re z<1/2\), both \(\Re\tan\pi z\) and
\(\Re\cot\pi z\) are positive, at every finite imaginary height.
For \(1/2<\Re z<1\), the cotangent real part is negative.
Thus all coefficients have the asserted signs. The endpoint forms
control both their leg and their own boundary variable even when
\(\epsilon_v=0\). Consequently
\[
                       -\Re\mathcal F''>0
 \tag{23}
\]
throughout (21), with a positive uniform lower bound on every compact
subchamber with bounded heights. This is a statement about the actual
complete-end phase, not about artificial endpoint vectors.

The exact sum (7) still extends outside (21). A global source theorem
requires a legal deformation of that full polytope, estimates for its
faces and cotangent aliases, and identification of a nonzero selected
coefficient. The central concavity in (23), the real boundary cubic
(14), and the global absolute reduction (12) do not by themselves give
those estimates. In particular we make no arbitrary mixed-word volume
claim here.

The scalar normalization already agrees with the expected open-source
Gaussian count. At regular real indices, the \(m\) vertex factors,
including the \(N^{k_4}\) carrier, contribute \(N^{m/2}\);
the \(m-1\) shared Gram factors contribute \(N^{-3(m-1)/2}\);
and the two factors in (3), using (10a), contribute
\(N^{a+b-4}\). If a legal deformation with a nonzero local symbol
and a nondegenerate critical point is subsequently proved, its
\(2m+2\) lattice variables supply \(N^{2m+2}\), and their Gaussian
integral supplies \(N^{-m-1}\). Their product is
\(N^{a+b-3/2}\). This count is conditional on that source deformation,
not a lower-bound deduction from the real-index symbol.

## 7. Reproduction

The all-level identities follow from the literal crossing coefficients
and the proved exact Gram contraction. The focused checker verifies the
phase and Schur algebra symbolically, then compares the original
normalized matrices and all complete boundary jets at several exact
finite levels. These finite checks are normalization diagnostics, not
the proof of the all-level identity or of a lower asymptotic bound.

```sh
python3 experiments/check_mixed_complete_boundary_sum.py
```

The result is saved in
[`research-mixed-complete-boundary-sum.json`](../repro/results/research-mixed-complete-boundary-sum.json).
