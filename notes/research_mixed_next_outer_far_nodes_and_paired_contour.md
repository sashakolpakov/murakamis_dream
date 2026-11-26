# Far physical nodes and the exact paired outer contour

Private finite-source deduction, 9 November 2026. The original outer
cosine observation can be localized to the physical angles
\(|u|<3/2+O(N^{-1})\), with a uniform exponential gap below the
continued selected action on the whole frequency interval. An exact
reflection then combines the upper and left sides of its finite
sampling rectangle with the lower and right sides. Both charges are
retained, including their equality at zero cosine frequency.

The resulting lower contour and right connector are still literal
unestimated currents. No global nonzero coefficient asymptotic or
adequate volume budget is claimed. No mathematical numerical
evaluation, saved-value arithmetic, or frozen-source edit is used.

## 1. Original source and normalization

Use
\[
\begin{gathered}
D=N-1,\quad q=e^{\pi i/N},\quad \eta_N=(-1)^D,\quad
M=\lceil N/2\rceil,\quad U=\lfloor N/2\rfloor-1,\\
c_j=2\cos((2j+1)\pi/N),\quad
u_j=\pi-(2j+1)\pi/N,\quad c_j=-2\cos u_j,\\
C_{N,3}=q^{3D^2/4},\qquad
Q_N^{\mathrm{full}}(u)=\mathcal K_{3,N}(-2,-2\cos u)
                         =P_{3,N}(0,u),\\
Q_N^{\mathrm{sh}}(u)=
\phi_N^{(x)}\!\left[
R_N(x)^3K_N^{\mathrm{ord}}(-2,x)
                 K_N^{<,\mathrm{ord}}(x,-2\cos u)\right],
\qquad
K_N^{<,\mathrm{ord}}(x,w)=\sum_{b=0}^{U}e_b(x)e_b(w).
\end{gathered}
\tag{1}
\]
Both sources have the original full inner Hermite trace. The first
edge of \(Q_N^{\mathrm{sh}}\) is full; only its outgoing edge is
shortened. Both angular sources are even entire functions.

The original response is
\[
\mathcal O_{N,k}=
\phi_N[R_N^3e_M\mathcal K_{3,N}(-2,\cdot)T_k(-\,\cdot/2)],
\qquad
0\le k\le\lfloor N/2\rfloor,\qquad
\delta=\frac12-\frac{k}{N}.
\tag{2}
\]
The exact low-edge reduction, [equations (11)--(14)](research_mixed_next_outer_exact_low_edge_reduction.md),
gives both the unchanged functional and the physical equalities
\[
Q_N^{\mathrm{full}}(u_j)=Q_N^{\mathrm{sh}}(u_j)
                            \quad(0\le j\le U).
\tag{3}
\]
This is not an off-grid equality. At odd levels the omitted simple
node has \(u=0\), and its outer radical weight is zero.

Define the unchanged parity factors
\[
a_N(u)=
\begin{cases}
\sin u,&N\text{ even},\\
\displaystyle\frac{\sin u\sin(u/2)}{\cos^2(\pi/(2N))},
   &N\text{ odd},
\end{cases}
\qquad
\chi_N=
\begin{cases}i,&N\text{ even},\\-1,&N\text{ odd}.
\end{cases}
\tag{4}
\]
In particular \(a_N(-u)=\eta_Na_N(u)\), and
\(|a_N(u)|\le4/3\) for real \(u\) and \(N\ge3\).
The consumed-normal weights are
\[
\mu_{j,N}=(-1)^{U+j}a_N(u_j)R_N(c_j)^3,\qquad 0\le j\le U.
\tag{5}
\]
These are the full original weights, not a new positive measure.
Their crossing values have modulus one. The exact Gaussian
crossing identity and the full-grid parity fold give
\[
\boxed{\quad
\mathcal O_{N,k}=\frac{\chi_N C_{N,3}}2
\sum_{j=0}^{D}a_N(u_j)Q_N^{\mathrm{sh}}(u_j)
 \exp N\left(\frac{3iu_j^2}{4\pi}-i\delta u_j\right).
\quad}
\tag{6}
\]
Indeed [the original fold, (4)--(6)](research_mixed_next_near_half_geometric_cosine_response.md)
uses \(Q_N^{\mathrm{full}}\); (3), evenness, and the zero odd
center weight replace its physical values exactly. Formula (6)
does not replace the source at any complex point. It retains
one outer scalar \(C_{N,3}\); no inner Gaussian approximation
has yet been inserted.

## 2. A bound on the continued charged-action loss

Keep the original selected action \(S(u)=S_3(0,u)\), with
\(M_3=\Re S(0)\), and its continued charged saddle
\[
\begin{gathered}
u_\delta=\beta-iK,\qquad
\Psi_\delta(u)=S(u)+\frac{3iu^2}{4\pi}-i\delta u,\\
\Gamma(\delta)=\Re\Psi_\delta(u_\delta),\qquad
\Gamma'(\delta)=-K,\qquad \Gamma(0)=M_3.
\end{gathered}
\tag{7}
\]
These are the original branch and additive constant of
[the full-interval continuation](research_mixed_next_selected_charged_curve_full_interval.md).
For \(0<\delta\le1/2\), its original unexponentiated equation and
the adopted [angle-depth guards](research_mixed_next_selected_charged_angle_depth_correlation.md)
give
\[
\begin{gathered}
0<\beta<4/3,\quad 0<K<\beta/2,\quad
c(u_\delta)=p+iq,\quad p>3/4,\quad 0<q<1/3,\\
w=c(u_\delta)\tan(u_\delta/2),\qquad
\operatorname{arsinh}w=X+i\nu=i(3u_\delta/2-\pi\delta),\\
D_0=\cos\beta+\cosh K>37/30,\\
\Re w=\frac{p\sin\beta+q\sinh K}{D_0}>0,\qquad
\Im w=\frac{q\sin\beta-p\sinh K}{D_0}.
\end{gathered}
\tag{8}
\]
The principal return has \(-\pi/2<\nu<\pi/2\).

**Lemma 1.** Throughout this selected interval,
\[
K<\frac{\pi\delta}{3}\quad(\delta>0),\qquad
\Gamma(\delta)>M_3-\frac{34}{275}
                          \quad(0\le\delta\le1/2).
\tag{9}
\]

*Proof.* If \(\nu\le0\), (8) gives
\(\pi\delta=3\beta/2-\nu\ge3\beta/2>3K\).
If \(\nu>0\), put \(x=\Re w\), \(y=\Im w\). Then
\(0<y/x<q/p<4/9\). On the segment \(x+iv\),
\(0\le v\le y\), the real part of \(1+(x+iv)^2\) is at least
one. The principal return is holomorphic there and real at \(x\);
therefore
\[
\nu=\int_0^y\Re\{1+(x+iv)^2\}^{-1/2}\,dv\le y.
\tag{10}
\]
The positive numerator in the last line of (8) is less than
\(\beta/3-3K/4\). Thus this latter expression is positive too,
so dividing by \(D_0>37/30\) preserves the upper comparison:
\[
\nu<\frac{10\beta}{37}-\frac{45K}{74},\qquad
\pi\delta>\frac{91\beta+45K}{74}>
                    \frac{227K}{74}>3K.
\tag{11}
\]
This proves the first assertion.

The adopted [depth bound](research_mixed_next_selected_charged_depth_bound.md)
also gives \(K<2/5\). Integrating (7), without any monotonicity
assumption on \(K\), yields
\[
\begin{split}
M_3-\Gamma(\delta)
&\le\int_0^{1/2}K(s)\,ds\\
&<\int_0^{1/2}\min\left\{\frac{\pi s}{3},\frac25\right\}\,ds
=\frac15-\frac6{25\pi}<\frac{34}{275}.
\end{split}
\tag{12}
\]
The switch is \(6/(5\pi)<1/2\), since \(\pi>3\).
The last comparison uses \(\pi<22/7\).
At \(\delta=0\) the second assertion follows directly from (7).
\(\square\)

## 3. Every far physical node is paid

For real \(0\le x\le\pi/2\), the original
[cubic continuation, (8),(13)](research_mixed_next_inner_three_cubic_continuation.md)
gives
\[
S'(x)=-\frac1\pi\operatorname{arsinh}\{c(x)\tan(x/2)\},
\qquad \Re c(x)>3/4,\quad \Im c(x)>0.
\tag{13}
\]
For a principal return \(\operatorname{arsinh}z=A+iB\) with
\(\Re z>0\), one has \(\Re z=\sinh A\cos B\le\sinh A\);
hence \(A\ge\operatorname{arsinh}(\Re z)\).
The real function \(\operatorname{arsinh}\) is concave and
vanishes at zero. Also
\((\operatorname{arsinh}\tan(x/2))'=\tfrac12\sec(x/2)\ge1/2\).
Consequently
\[
\begin{split}
\Re\operatorname{arsinh}\{c(x)\tan(x/2)\}
&\ge\operatorname{arsinh}\{(3/4)\tan(x/2)\}\\
&\ge\frac34\operatorname{arsinh}\tan(x/2)\ge\frac{3x}{8}.
\end{split}
\]
Integrating with the original constant proves
\[
s(x):=\Re S(x)\le M_3-\frac{3x^2}{16\pi},
                                \qquad 0\le x\le\pi/2.
\tag{14}
\]

At physical double nodes in this interval,
[the complete physical packet, (4)](research_mixed_next_inner_three_physical_outgoing_packet.md)
gives the corresponding uniform finite upper bound for
\(Q_N^{\mathrm{sh}}\). At every remaining physical double
node \(x=u_j\ge\pi/2\), the distinct full-source theorem
[for the upper physical half-period, (3)](research_mixed_next_inner_three_upper_physical_majorant.md)
gives, for any prescribed \(\tau>0\),
\[
|Q_N^{\mathrm{sh}}(u_j)|
 \le C_\tau
   e^{N\{s(\pi/2)-\kappa_0(u_j-\pi/2)+\tau\}},
                         \qquad \kappa_0>0.
\tag{15}
\]
Its far derivative samples, full inner normal contributions and
odd central contribution have already been included in that
source proof. Dropping the favorable slope in (15) is legitimate.

For \(3/2\le x\le\pi/2\), the loss in (14) is at least
\(27/(64\pi)>189/1408\). For \(x\ge\pi/2\), (14) at
\(\pi/2\) gives loss \(3\pi/64>27/(64\pi)\).
Using (3), evenness and (15), all original grid nodes with
\(|u_j|\ge3/2\) therefore satisfy
\[
|Q_N^{\mathrm{full}}(u_j)|=
|Q_N^{\mathrm{sh}}(u_j)|
 \le C_\tau N^A e^{N\{M_3-189/1408+\tau\}}.
\tag{16}
\]
The equality in (16) is only being used at the noncentral
double nodes and their reflected copies.

**Theorem 2.** Uniformly for all integers \(k\) in (2), both
parities and every subset of the original grid with
\(|u_j|\ge3/2\), the sum of the absolute values of its terms
in (6) is bounded by
\[
C\exp N\{\Gamma(\delta)-1/100\}.
\tag{17}
\]
The same conclusion holds for the corresponding sum with
the literal positive-node weights \(\mu_{j,N}\) and
\(\cos(k u_j)\).

*Proof.* The real Gaussian and character have modulus one,
and (4)--(5) bound all weights. There are at most \(N\)
terms. The exact comparison is
\[
\frac{189}{1408}-\frac{34}{275}
 =\frac{4103}{387200}
 =\frac1{100}+\frac{231}{387200},
\qquad
\frac{231}{387200}>\frac1{2000}.
\tag{18}
\]
Take \(\tau=1/4000\) in (15), and absorb all fixed polynomial
factors into another \(1/4000\) for sufficiently large \(N\).
Equations (9),(16),(18) prove (17).
No relative packet error has been summed as if it had a common
phase. \(\square\)

## 4. An exact two-current rectangle on the whole frequency interval

Write the grid as \(2\pi(\ell+\rho_N)/N\), with
\(\rho_N=1/2\) for even \(N\) and \(0\) for odd \(N\). Set
\[
T_N=\frac{2\pi}{N}
\left(
\left\lceil\frac{3N}{4\pi}-\rho_N-\frac12\right\rceil
                         +\rho_N+\frac12\right).
\tag{19}
\]
Then
\[
\frac32\le T_N<\frac32+\frac{2\pi}{N}<\frac{\pi}{2}
\tag{20}
\]
for sufficiently large \(N\). Both \(\pm T_N\) are grid
midpoints and obey \(\eta_Ne^{-iN(\pm T_N)}=-1\).
For any fixed \(h>0\), let \(\mathcal R_{N,h}\) be the
positively oriented rectangle with vertices \(\pm T_N\pm ih\).
Define, for any real charge \(\sigma\),
\[
H_N(u)=\frac1{1-\eta_Ne^{-iNu}},\qquad
f_{N,\sigma}(u)=a_N(u)Q_N^{\mathrm{sh}}(u)
             \exp N\left(\frac{3iu^2}{4\pi}-i\sigma u\right).
\tag{21}
\]
The source in \(f\) is entire, and the residue of \(H_N\)
at each grid point is \(1/(iN)\). Hence the exact finite
sampling identity and Theorem 2 give
\[
\mathcal O_{N,k}
=\frac{\chi_N C_{N,3}N}{4\pi}
        \oint_{\mathcal R_{N,h}}H_N(u)f_{N,\delta}(u)\,du
 +O\!\left(e^{N\{\Gamma(\delta)-1/100\}}\right).
\tag{22}
\]
Only physical nodes outside the rectangle were estimated.
No bound on any of its complex sides is asserted in (22).

Let \(B_{N,h}\) be the bottom segment, oriented left to
right, and \(V_{N,h}\) the right segment, oriented upwards.
There is the exact identity
\[
\boxed{\quad
\oint_{\mathcal R_{N,h}}H_Nf_{N,\delta}
 =
\int_{B_{N,h}}H_N(f_{N,\delta}+f_{N,1-\delta})
 +\int_{V_{N,h}}H_N(f_{N,\delta}+f_{N,1-\delta}).
\quad}
\tag{23}
\]
In particular, for the integer frequency in (2),
\[
f_{N,1-\delta}(u)=e^{-2iku}f_{N,\delta}(u).
\tag{24}
\]

To check every sign in (23), use
\[
H_N(-u)=1-H_N(u),\qquad
f_{N,\delta}(-u)=\eta_Nf_{N,-\delta}(u),\qquad
H_N(u)-1=\eta_Ne^{-iNu}H_N(u).
\tag{25}
\]
Reflection \(u=-v\) maps the top, originally right to
left, onto the bottom with the same left-to-right endpoints;
the differential contributes a minus sign. Its contribution is
therefore
\[
-\eta_N\int_{B_{N,h}}(1-H_N(v))f_{N,-\delta}(v)\,dv
                 =\int_{B_{N,h}}H_N(v)f_{N,1-\delta}(v)\,dv.
\tag{26}
\]
The left side, originally oriented downwards, maps in exactly
the same way to \(V_{N,h}\), giving its second charge in
(23). This proves (23), including both complete vertical
currents and the full rational sampling multiplier.
Neither \(f\) nor the cubic Gaussian is declared periodic.

At zero cosine frequency, \(k=0\) and \(\delta=1/2\), the
factor in (24) is exactly one. Thus the paired integrand is
exactly \(2H_Nf_{N,1/2}\). The upper alias is not discarded
as exponentially smaller. At the other endpoint, even
\(N\) and \(k=N/2\), the original response is exactly zero
because every physical \(\cos(Nu_j/2)\) vanishes. Formulas
(22)--(24) retain this endpoint without a nonzero assertion.

## 5. The paired factor near the selected saddle

Fix \(0<\delta_1\le1/2\). Compactness and the original selected
curve give
\[
K_{\min}=\min_{\delta_1\le\delta\le1/2}
                            (-\Im u_\delta)>0.
\tag{27}
\]
On a sufficiently small fixed complex neighborhood of this
compact curve, \(\Im u\le-K_{\min}/2\). Consequently, for
every integer \(k\ge1\),
\[
|e^{-2iku}|\le e^{-kK_{\min}},\qquad
|1+e^{-2iku}|\ge1-e^{-K_{\min}}>0.
\tag{28}
\]
For \(k=0\), this last factor is two. Its fixed derivatives
are uniformly bounded on the neighborhood: the \(r\)-th
derivative of its nonconstant term has modulus at most
\((2k)^r e^{-kK_{\min}}\), whose supremum over positive
integers is finite. Its inverse and all fixed derivatives
on a smaller neighborhood are uniformly bounded as well.

Thus the exact paired factor can be retained inside a local
selected Gaussian amplitude, including integer sequences
approaching \(k=0\). It supplies no cancellation zero there.
This statement alone does not permit a Gaussian evaluation:
the remainder of the bottom current and the right connector
in (23) must still be estimated with their complete sources.
In particular this note gives no complex-source bound on
the negative lower half or the central imaginary axis.

The new conclusions are the paid physical tail (17), the
complete finite reduction (22)--(24), and the uniform local
property (28). They do not prove the full cosine response
asymptotic on \(0\le\delta\le1/2\), suppress the entire outer
correction, or establish a new family of filling theorems.

## Frozen source bindings

- Original parity fold and observation:
  19a62beac1f4e2ef3c900d18d402c316b2cf098cd7c32753924824fe2aedcc02.
- Exact outgoing low-edge reduction:
  76524c28bdbafafe8922993093e3e5b4447ec033e4b0dd3928295047bfde797a.
- Physical positive-half packet:
  c43064953e7d3bfa92a6ecc05725719661e45d0b6bfca76fe1b78a28c68de4f3.
- Complete upper physical majorant:
  6fd4d8c0d67e184312f0d1106b112ac00a965f7d40716aae8ac7b502eb709c18.
- Original cubic and action derivative:
  8a8ef3f93a4ab44724d43f7bb9b15c5f8210d4649f79d1f0d4c0ec277801f41a.
- Full selected charged curve:
  6828459338fff642bf52b425120ed806d39bd9847d8df5ea5db8a14f0859da0c.
- Selected upper depth:
  f3b0b8f8e14adb8beff461e53ec20cdcb7afb4dc07bda3e1247116b55e13c017.
- Original angle-depth guards and signed return:
  49d0d81bb39dcdb8946893c8bc0b712e00b2eaad15b3f5476b62736fce1df1f4.
- Consumed-normal observation:
  cbbc62951666d06e0ae77b29f49f563d91c2024dc8da900ae996144d7db39dab.
- Original Gaussian crossing:
  f81b9fc3edc2504c5250ad283bf0ceff191a1fc3a310c00fdb57602362f0bf4a.
