# The complete first sum on the upper radial connection for 444

Private written proof, 11 November 2026. For an actual word beginning
with three four-twist blocks, the complete first polynomial can be
carried along the positive real segment from \(1\) to \(e^{\pi/50}\).
Both second Fourier terms have a strict bound below the original
geometric action, on a fixed complex neighborhood of the segment.
This includes the vertical connection from \(y=0\) to \(y=i/100\)
in the additive second coordinate.

The proof uses a stronger type-four lower bound already contained in
the three-factor action comparison. It combines that bound with
exact finite-product estimates. The first integration is complete;
no restriction to its central interval is made.

## 1. The original finite source

Fix the actual positive three/four word and reference of the
[complete first-sum seam theorem](research_mixed_complete44_second_period_seam_collar.md),
with length \(m\ge4\) and initial types \(444\). Put
\[
 P=[11/50,9/20],\qquad z=v+ic_3,\quad v\in P,\qquad
 -51/500\le c_3\le-1/1000,\qquad Z=e^{-2\pi iz}.
 \tag{1}
\]
The third conditional index is ordinary, including when \(m=4\);
its following terminal incidence is unchanged. Keep the same
ordinary incoming color \(w\), logarithmic lifts, and all scalars.

With \(\zeta=e^{-2\pi i/N}\), define
\[
 P_j=(\zeta;\zeta)_j,\quad S_j=|P_j|,\quad
 p_j(V)=(\zeta V;\zeta)_j,\qquad D=N-1.
\]
The complete factors are
\[
\begin{split}
 U_N(w,X)&=\sum_{i=0}^{D}H_N(w,\zeta^{-i})p_i(X)/P_i^2,\\
 C_N(X,Y)&=\sum_{j=0}^{D}X^{-j}p_j(X)p_j(Y)/P_j^3,\\
 f_N(w,Y)&=N\operatorname{CT}_X
       [U_N(w,X)d_N(X)(1+X^{-N})C_N(X,Y)].
\end{split}                                                        \tag{2}
\]
Here \(d_N\) is the original degree-\(D\) interpolation polynomial,
with \(d_N(\zeta^j)=P_j^{-1}\). The first root filter is exactly
\[
 f_N(w,Y)=\sum_{a=0}^{D}
                 \frac{U_N(w,\zeta^a)}{P_a}C_N(\zeta^a,Y).
 \tag{3}
\]
There is no additional factor two in (3). The two coefficient
integrals in (2) together equal this one physical sum.

For the second Fourier choice \(\sigma\in\{0,1\}\), retain
\[
 {\cal D}_{\sigma,N}(w,Y,Z)
       =f_N(w,Y)d_N(Y)Y^{-\sigma N}C_N(Y,Z).
 \tag{4}
\]
The outgoing modulus allocation is \(|d_N(Z)|^{1/2}\), including
at its zeros. The second extraction measure is still \(+N\,dy\),
with \(Y=e^{-2\pi iy}\).

Write \(\Lambda_{123}(z)\) for the exact affine action in the seam
theorem. In its original notation,
\[
\begin{split}
 F_{123}&=\Psi(e,z_1)+Q_1(s_2;z_1,z_2)+Q_1(s_3;z_2,z_3)
                    -g(z_1)-g(z_2)-\tfrac12g(z_3),\\
 p_R&=g'(s_3^*+r_3)-\tfrac32g'(r_3),\\
 \Lambda_{123}(z)&=\Re F_{123,*}+\Re\{p_R(z-r_3)\}.
\end{split}                                                        \tag{5}
\]
Every star belongs to the same coupled reference. This proof makes
no change to the absolute action or its outgoing marginal.

**Theorem.** There is a fixed complex neighborhood \({\cal V}\) of
\([1,e^{\pi/50}]\), a fixed ordinary-color disk \({\cal W}\) about
\(-2\), and constants \(C,B,N_0\) such that
\[
 |{\cal D}_{\sigma,N}(w,Y,Z)|\,|d_N(Z)|^{1/2}
       \le C N^B e^{N\{\Lambda_{123}(z)-1/200\}}
 \tag{6}
\]
for \(N\ge N_0\), both parities, both \(\sigma\), every \(z\) in
(1), and \(w\in[-2,2]\cup{\cal W}\), \(Y\in{\cal V}\).
Every fixed derivative in \(Y\) and \(w\) has the same rate on
smaller fixed neighborhoods, with a possibly different polynomial
prefactor. The outgoing modulus factor is not differentiated.

The theorem pays the complete density on the upper radial connection
and on short angular segments at its upper end. It does not estimate
the entire second period or assert noncancellation for its integral.

## 2. The stronger type-four action floor

In the [affine-floor proof](research_mixed_complete44_three_factor_affine_floor.md),
equation (11) compares a particular raw profile trial \(T_\beta\)
with the original action:
\[
 T_\beta(z)-\frac{\beta}{2}\Re g(z)
                <\Lambda_{123}(z)-1/100.
 \tag{7}
\]
The comparison is between real action profiles, before any finite
summation. Equations (46)--(48) in that proof give
\[
 T_0>\frac73+\frac{193}{357000}.
 \tag{8}
\]
The same paragraph records that the type-four expression \(T_1\)
improves this lower bound by \(39/400\). This improvement is the
difference between its already established rational witnesses for
\(2\lambda_*+\tfrac32 b_2\) and
\(\tfrac32\lambda_*+2b_2\); it does not require a new evaluation
of either action. Taking \(\beta=1\) in (7) therefore yields
\[
 \boxed{\quad
 \Lambda_{123}(z)+\tfrac12\Re g(z)>
                         \frac73+\frac{43}{400}.
 \quad}                                                           \tag{9}
\]
We have discarded the additional positive term in (8).
The bound is uniform on the original independent third interval
at its actual negative height and for either following type.

## 3. Complete finite bounds on the positive radial segment

The complete seam theorem, equations (12), (13), and (20), supplies
the following three estimates, with an arbitrarily small total
rate allowance:
\[
\begin{split}
 \sup_{|X|=1}|U_N(w,X)|
   &\le C_\tau N^{B_\tau}e^{N(b_1+c_{\rm b}+\tau)},\\
 \sup_{|X|=1}|d_N(X)|
   &\le C N^B e^{Nc_{\rm b}/2},\\
 \sup_{|V|\le1}\sum_{j=0}^{D}\frac{|p_j(V)|}{S_j^2}
   &\le C_\tau N^{B_\tau}e^{N(7/15+\tau)},
 \qquad b_1=\frac{433}{500},\quad c_{\rm b}<\frac{13}{40}.
\end{split}                                                        \tag{10}
\]
They include every summation index and keep \(H_N\) coherent.
Their all-real-color and fixed complex-color versions are part of
that source. The actual \(Z\) in (1) lies in the last disk.

For \(R\ge1\), Lemma 1 of the
[upper radial product theorem](research_mixed_next_upper_radial_seam.md)
proves the exact inequalities
\[
 a_j(R):=\frac{|p_j(R)|}{S_j}\le R^D,\qquad
                    R^{-j}a_j(R)\le R^{D/4}.
 \tag{11}
\]
Here is the finite mechanism. The factors of
\(b_j=R^{-j/2}a_j\) are at least one and invariant under
\(k\mapsto N-k\). The full products satisfy
\[
 a_D=\frac1N\sum_{k=0}^{D}R^k\le R^D,\qquad
 b_D\le R^{D/2}.
\]
For \(2j\le D\), the first and last \(j\) factors of \(b_D\)
are disjoint and equal, so \(b_j^2\le b_D\).
For \(2j\ge D\), use \(b_j\le b_D\). These two cases give
the second inequality in (11), including both parity endpoints.

Take \(R=e^c\), \(0\le c\le\pi/50\). Equations (10)--(11) give
\[
\begin{split}
 \sup_{|X|=1}|C_N(X,R)|
       &\le C_\tau N^{B_\tau}e^{N(7/15+c+\tau)},\\
 |C_N(R,Z)|
       &\le C_\tau N^{B_\tau}e^{N(7/15+c/4+\tau)}.
\end{split}                                                        \tag{12}
\]
The incoming monomial \(R^{-j}\) is included in the second line.
The first line uses \(|X^{-j}|=1\).

Evaluate both coefficient integrals in (2) on the full unit circle.
The factor \(|1+X^{-N}|\le2\), its fixed integration length, and
the original factor \(N\) have polynomial cost. Thus
\[
 |f_N(w,R)|\le C_\tau N^{B_\tau}
       e^{N\{b_1+\tfrac32c_{\rm b}+7/15+c+\tau\}}.
 \tag{13}
\]
This is a bound on the complete first polynomial. No first-coordinate
region, physical row, or Fourier term has been omitted.

The exact polynomial identity
\[
 d_N(Y)=\frac1N\sum_{j=0}^{D}\frac{p_j(Y)}{P_j}
 \tag{14}
\]
retains its original forcing. In particular
\[
 |d_N(R)|R^{-\sigma N}\le R^{(1-\sigma)N},
 \qquad \sigma=0,1.
 \tag{15}
\]
For \(\sigma=1\) the sharper right side \(R^{-1}\le1\)
is available, but is unnecessary.

Combining (12)--(15), and assigning a single total allowance, gives
\[
 |{\cal D}_{\sigma,N}(w,R,Z)|
 \le C_\tau N^{B_\tau}
 e^{N\{b_1+\tfrac32c_{\rm b}+14/15+(9/4-\sigma)c+\tau\}}.
 \tag{16}
\]
The worse sector is the unselected one. The selected monomial has
been retained rather than silently assigned to both sectors.

## 4. A fixed complex neighborhood

Let \(|Y-R|\le\varepsilon<1/2\), with
\(1\le R\le e^{\pi/50}\). The exact factor identity
\[
 |1-R\zeta^k|^2
      =R|1-\zeta^k|^2+(R-1)^2\ge|1-\zeta^k|^2
\]
and the original sine-chord product estimate give
\[
 |p_j(Y)|\le |p_j(R)|e^{N\Omega(\varepsilon)},\qquad
 \Omega(\varepsilon)=\log(1+\varepsilon/2)
       +\frac{\varepsilon}{2}\log(1+2/\varepsilon).
 \tag{17}
\]
In particular \(\Omega(\varepsilon)\to0\). This bounds every
original finite product, including all its zeros; no quotient
through a source zero is taken.
Also
\[
 |Y|^{-j}\le R^{-j}(1-\varepsilon)^{-N},\qquad
 |Y|^{-\sigma N}\le R^{-\sigma N}(1-\varepsilon)^{-\sigma N}.
 \tag{18}
\]
Apply (17) once to the first conditional factor, once to the
next conditional factor, and once to (14). Apply (18) to the
next incoming monomial and to the second Fourier monomial.
Equations (13)--(16) remain valid with added rate at most
\[
 E(\varepsilon)=3\Omega(\varepsilon)-2\log(1-\varepsilon)
                          \longrightarrow0.
 \tag{19}
\]
This proof keeps both coefficient integrals for \(f_N\) inside the
estimate; it does not infer a neighborhood bound from values on
the segment alone.

## 5. Calibration and the original integration density

The unallocated bound in (16) is strictly below (9). Indeed,
\[
\begin{split}
 &\left(\frac73+\frac{43}{400}\right)
   -\left(\frac{433}{500}+\frac{39}{80}+\frac{14}{15}\right)
        =\frac{77}{500},\\
 &\frac{77}{500}-\frac{9\pi}{200}
       >\frac{77}{500}-\frac{99}{700}
        =\frac{11}{875}.
\end{split}                                                        \tag{20}
\]
Only \(\pi<22/7\) was used. There is no action evaluation in
this comparison.

On the third interval (1), the original Fourier-weight estimate gives
\[
 |d_N(Z)|^{1/2}
        \le C_\tau N^{B_\tau}e^{N\{-\Re g(z)/2+\tau\}}.
 \tag{21}
\]
Its factorial upper alternative dominates there since
\(\Re g(z)<0\); this assertion requires no nonvanishing of
the actual polynomial.

Choose a fixed \(\varepsilon>0\) such that
\(E(2\varepsilon)<1/400\). Allocate a total allowance less
than \(1/400\) to (10), (12), (13), the color neighborhood,
and (21). Since \(11/875>1/100\), equations (9), (16),
and (19)--(21) give (6) on the larger tube of radius
\(2\varepsilon\). Restricting to radius \(\varepsilon\) and
smaller color disks gives the derivative statements by Cauchy's
formula. At fixed \(Z\), its modulus allocation is constant in
these differentiated variables, even if it vanishes.

The logarithmic preimage of this tube contains the entire segment
\(\{ih:0\le h\le1/100\}\), as well as a fixed neighborhood
of it. It therefore includes short angular pieces at both
ends of the second period, at height \(1/100\).
Integrating any fixed finite-length path there with \(+N\,dy\)
preserves the same exponential gap. The first density \(N\)
is already present in (13); no additional root-average factor
or phase is introduced.

The theorem gives a complete first-sum estimate on this radial
connection. The rest of the selected second contour, and the
nonzero asymptotic for its full contraction, remain separate.

## Direct source bindings

| Direct source | SHA-256 |
|---|---|
| research_mixed_complete44_second_period_seam_collar.md | e203f8041ddcc3c002d09de0a5d94a458f2499a3f55325fce27126c3c7b66a6c |
| research_mixed_complete44_three_factor_affine_floor.md | 112f3b5a8d40c7a3bb770b8deae7b189c4729235851d8a2036f8869edc332b7d |
| research_mixed_next_upper_radial_seam.md | b351d9e4177b9a9454b2a748f00b159a00c7209954164dccac793c9eb5aac3bb |
| research_mixed_fourier_weight_continuation.md | 0bae41d83f414eb91fd137de1242120a11408147d56ec752e466ca5ed7e7f48e |

The full written proof and all four directly used source implications
have been read by the author, and all four bindings checked.
Independent full proof and direct-source review is required before
adoption. No mathematical numerical evaluation, saved-value arithmetic,
import, test, compilation, or frozen-source modification was used.
