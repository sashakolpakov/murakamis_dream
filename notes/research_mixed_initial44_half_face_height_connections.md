# Both first-height connections at the initial four/four half face

Private written proof, 10 November 2026. The first coordinate can
connect its actual negative height to zero, or its selected positive
height to zero, at real part one half. The neighboring coordinate
stays on its entire plateau at its actual negative height. The proof
pays the complete cap and the complete conditional polynomial,
including the physical end blocks in the latter's upper envelope.
It also retains profilewise bounds at the resulting real face.

These are two specified vertical contributions. Neither vertical
is a full period, and no subsequent real interval is included.

## 1. Actual source and statement

Use the actual coupled reference and original primitives of
[the selected upper-right theorem](research_mixed_selected44_upper_right_complete_pair.md).
The positive three/four word has length \(m\ge3\) and begins with
four and four. Write
\[
 a_*=a_0+ic,\qquad b_*=b_0+id,\qquad
 .246<a_0<.350,\quad -.078<c<-.020,
 \qquad -.102\le d\le-.001 .
 \tag{1}
\]
The cap private height is \(h_e\in(-.051,-.019)\); the actual
ordinary private height belongs to \([-.108,0]\). These remain
the actual coupled heights, including the original length-three
attachment. No independent reference substitution is made.
Set
\[
 H=\frac1{100},\quad a_h=\frac12+ih,\quad
 b=z+id,\quad z\in P=[11/50,9/20],\quad
 \kappa=\frac1{2500000},\quad
 \delta_R=\kappa(9/20-a_0)^2>0 .
 \tag{2}
\]
In particular \(\delta_R>\kappa/100\).
With \(q_N=e^{-2\pi i/N}\), \(P_j=(q_N;q_N)_j\),
\(p_j(X)=(q_NX;q_N)_j\), retain exactly
\[
\begin{split}
 X_h&=e^{-2\pi ia_h}=-e^{2\pi h},\qquad Y=e^{-2\pi ib},\\
 U_{1,N}(w,X)&=\sum_{i=0}^{N-1}H_N(w,q_N^{-i})p_i(X)/P_i^2,\\
 C_{1,N}(X,Y)&=\sum_{j=0}^{N-1}X^{-j}p_j(X)p_j(Y)/P_j^3 .
\end{split}
\tag{3}
\]
Let \(\Lambda(z)\) be the unchanged geometric affine rate in
equation (4) of the selected half-face theorem, with its original
additive constant and outgoing marginal.

**Theorem 1.** For every \(\tau>0\), both parities and all
real ordinary colors \(w\in[-2,2]\) satisfy
\[
\begin{split}
 &|U_{1,N}(w,X_h)C_{1,N}(X_h,Y)d_N(X_h)|
                  |d_N(Y)|^{1/2}\\
 &\hspace{15mm}\le C_\tau N^{A_\tau}
       e^{N\{\Lambda(z)-\delta_R/2+\tau\}},
                   &&c\le h\le0,\\
 &|U_{1,N}(w,X_h)C_{1,N}(X_h,Y)d_N(X_h)X_h^{-N}|
                  |d_N(Y)|^{1/2}\\
 &\hspace{15mm}\le C_\tau N^{A_\tau}
       e^{N\{\Lambda(z)-\delta_R/2+\tau\}},
                   &&0\le h\le H .
\end{split}
\tag{4}
\]
Fixed sufficiently small ordinary-color disks have the same bounds
at a separately reserved arbitrary rate allowance; fixed derivatives
on smaller disks cost a polynomial factor. Integrating either oriented
vertical with the original measure \(+N\,da\) and exterior scalar
preserves the bound. The second vertical may be oriented from \(H\)
down to zero.

At this face \(\Re g(a_h)=0\). The complete Fourier upper bound has
rate \(\max\{-\Re g(a_h),2\pi h_+\}\). It is therefore zero for
the first line of (4), and remains zero after the selected monomial
subtracts \(2\pi h\) in its second line. This retains both forcing
alternatives and makes no division by a finite Fourier polynomial.
The outgoing halfweight retains rate \(-\Re g(b)/2\).

## 2. One complete cap envelope throughout the height interval

Use the original five bare cap profiles
\[
\begin{array}{ll}
 A_0(h)=\max_{.27\le u\le.49}\Re\Psi(u+ih_e,a_h),&
 A_L(h)=\Re\Psi(.27,a_h),\quad
 A_R(h)=\Re\Psi(.49,a_h),\\
 A_-(h)=\max_u\Re\Psi(u-.055i,a_h)-.11\pi,&
 A_+(h)=\max_u\Re\Psi(u+.04i,a_h)-.08\pi .
\end{array}
\tag{5}
\]
Here \(\Psi\) is the same type-four bare phase as in the selected
half-face source. Its incoming dependence is precisely
\(g(e+a)-g(a)\). Put
\[
 E_*=\frac35+2\pi H+\frac{\log4}{100}<\frac{69}{100},
 \qquad
 \mathcal A(h)=\max\{A_0(h),A_L(h),A_R(h),A_-(h),A_+(h),E_*\}.
 \tag{6}
\]
Then, uniformly for \(c\le h\le H\),
\[
 |U_{1,N}(w,X_h)|
 \le C_\varepsilon N^{A_\varepsilon}
                         e^{N\{\mathcal A(h)+\varepsilon\}} .
 \tag{7}
\]

Here is the full finite-source check. The entire cap rectangle
\(E_c=[.27,.49]+i[-.055,.04]\) and \(a_h\) lie in the
domain of the upper-target cap theorem. The numerator \(a_h+e\)
has real part between \(.77\) and \(.99\), so no numerator
period wall is crossed. Its original private convexity and
weighted-side arguments bound the two zero-mode joins and four
weighted vertical half-sides by (5). Both horizontal aliases keep
their original penalties. The coherent coefficient continuation,
the \(+N\) zero mode and the \(N/(2i)\) residue multipliers are
unchanged.

The lower compact physical rows reduce to the current real cut
\(.27\), by Section 2 of upper-target extension, valid throughout
this incoming-height interval. For the upper compact rows, their
exact rate is
\(\lambda(e)+I_{1/2,e^{2\pi h}}(e)-J(e)\).
Its index derivative is
\[
 \lambda'(e)-J'(e)
       +\log|1-e^{2\pi h}e^{-2\pi i(1/2+e)}|<0
                         \quad(.49\le e<1).
 \tag{8}
\]
Indeed the first difference is less than \(-6/5\) on the bridge
to \(1/2\) and at most \(-\log4\) thereafter. The last term is
at most \(\log(1+e^{2\pi H})<3/4\), as proved in the selected
upper-right source. Thus all these rows reduce to the current
right cut.

For the true ends use the exact finite estimates in Section 3 of
that source. On \(|X|\le1\) they have rates below \(1/4\) and
\(3/5\). On \(1\le|X|\le e^{2\pi H}\), the reciprocal
polynomial bound supplies the extra factor \(|X|^i\) at the
upper end; a common sufficiently small fixed end width bounds
its rate by \(3/5+2\pi H<E_*\). The lower-end entropy still
tends uniformly to zero. These statements keep the actual last
rows, including the odd endpoint, and the full \(H_N(w,q_N^{-i})\);
no coherent coefficient is replaced by its separate Newton moduli
except inside the already proved true-end estimate. This proves (7)
with all rows and currents.

Every fixed private point in (5) satisfies
\[
 \frac{d}{dh}\Re\Psi(e,a_h)
       =-\Arg(1-e^{-2\pi i(e+a_h)})\in(0,\pi),\qquad
 \frac{d^2}{dh^2}\Re\Psi(e,a_h)
       =-\pi\Re\cot\pi(e+a_h)>0 .
 \tag{9}
\]
The incoming base argument is zero because \(X_h<0\), and
\(\Re\cot\pi a_h=0\). Both signs follow from
\(.77\le\Re(e+a_h)\le.99\) on the original regular strip.
The profile penalties are independent of \(h\).
Consequently \(\mathcal A\) is convex and nondecreasing, and
for \(h_1\le h_2\)
\[
       0\le\mathcal A(h_2)-\mathcal A(h_1)\le\pi(h_2-h_1).
 \tag{10}
\]
These properties concern explicit complete-source upper profiles,
not the logarithm of the modulus of a signed finite cap.

## 3. Convexity of the original conditional critical action

Retain the original phase
\[
 Q(s;a,b)=g(a+s)+g(b+s)-3g(s)-g(a)-g(b)+2\pi ias .
 \tag{11}
\]
The positive-incoming action theorem and Proposition 2 of the
selected upper-right theorem give the same simple critical point,
with zero logarithmic lift, throughout \(c\le h\le H\):
\[
 Q_s(s_*;a_h,b)=0,\qquad
 \frac2{25}<\Re s_*<\frac12,\quad
 |\Im s_*|<\frac{\log5}{2\pi},\qquad
 \Theta(a_h,b)=Q(s_*;a_h,b).
 \tag{12}
\]
The critical point is the original continued root; no new root is
selected by a polynomial equation.

Write \(C(q)=\Re\cot\pi q\). On the strip in (12), the proof of
Section 5 of the lower-output reduction gives
\[
           B:=3C(s)-C(b+s)>0 .
 \tag{13}
\]
For completeness, if \(\Re(b+s)\ge1/2\), this follows from
\(C(s)>0\) and \(C(b+s)\le0\). Otherwise that proof gives
\(C(s)>133/488\), \(C(b+s)<4/5\), and therefore
\(B>43/2440\). These estimates use the actual outgoing
real interval and the critical height strip, not a sign
assumption on the incoming height.

At \(a=a_h\), put \(D=-C(a+s)>0\). The full negative real
Hessian of \(Q\) in \((a,s)\), divided by \(\pi\), is
\[
 -\frac1\pi\Re Q''=
 \begin{pmatrix}D&D\\D&D+B\end{pmatrix}\succ0.
 \tag{14}
\]
The chirp's mixed derivative is purely imaginary and does not
alter (14). Let \(v=(1,-Q_{ss}^{-1}Q_{sa})^T\). Since
\(Q''v=(\Theta_{aa},0)^T\), symmetry of the holomorphic Hessian
gives
\[
 \Re\Theta_{aa}=\Re(v^*Q''v)
                   =v^*(\Re Q'')v<0.
 \tag{15}
\]
Here the equality of real parts uses that both real and imaginary
parts of \(Q''\) are real symmetric matrices. Thus
\[
                  \frac{d^2}{dh^2}\Re\Theta(a_h,b)>0 .
 \tag{16}
\]
In particular \(\mathcal A(h)+\Re\Theta(a_h,b)\) is convex.
The independently proved incoming multiplier also gives
\[
                  \frac d{dh}\Re\Theta=-\Arg\omega<0 .
 \tag{17}
\]
Equation (17) will preserve a stronger true-end reserve at zero;
convexity (16) is what compares the full cap envelope.

## 4. Physical low and high profiles: different height arguments

Keep the literal continuous physical-row rate
\[
 E_h(t)=I_{1/2,e^{2\pi h}}(t)
       +I_{z,e^{2\pi d}}(t)-3J(t)-2\pi ht,\qquad0\le t\le1,
 \quad
 I_{x,r}(t)=\int_0^t\log|1-re^{-2\pi i(x+v)}|\,dv .
 \tag{18}
\]
It includes the incoming chirp and the last-row limit.

For \(0\le t\le2/25\), there is no incoming numerator wall.
Exact differentiation gives
\[
 \frac{d^2}{dh^2}E_h(t)
   =-\pi C(1/2+t+ih)\ge0 .
 \tag{19}
\]
Thus each \(\mathcal A(h)+E_h(t)\) is convex on \([c,H]\).

For \(1/2\le t\le1\) and \(h<0\), use the original postwall
disk branch, whose argument is nonnegative. Then
\[
 \frac d{dh}E_h(t)
    =-\Arg(1-e^{-2\pi i(t-1/2+ih)})-2\pi t
    \le-\pi .
 \tag{20}
\]
Together with (10), this shows
\(\mathcal A(h)+E_h(t)\) is nonincreasing on \([c,0]\).
For \(h\ge0\), the exact modulus identity
\[
 |1-e^{2\pi h}e^{-2\pi i(1/2+v)}|
 =e^{2\pi h}
       |1-e^{-2\pi h}e^{-2\pi i(1/2+v)}|
 \tag{21}
\]
cancels the entire chirp in (18). Differentiation now gives
\[
 \frac d{dh}E_h(t)
   =\Arg(1-e^{-2\pi i(t-1/2-ih)})\ge0
                 \qquad(1/2\le t\le1,\ h>0).
 \tag{22}
\]
Hence \(\mathcal A(h)+E_h(t)\) is nondecreasing on \([0,H]\).
At \(t=1/2,1\) or \(h=0\), use the continuous integrated
limits; no logarithmic summand is divided out. The high block
is therefore bounded by the larger of its two original endpoint
profiles, despite not being a convex height profile.

We also record that every physical row is nonincreasing in \(h\)
on the negative interval before inserting the cap. For \(t\le1/2\),
the strip argument at \(1/2+t+ih\) lies between \(-2\pi t\)
and zero, so
\[
                 \partial_h E_h(t)
      =-\Arg(1-e^{-2\pi i(1/2+t+ih)})-2\pi t\le0 .
 \tag{23}
\]
For \(t\ge1/2\) use (20). This separate observation applies
to a constant true-end ceiling.

## 5. The two endpoint calibrations and their preserved gaps

At \(h=c\), the complete lower cap proof supplies its original
allocated half-face plane \(B_*>149/200\). Every profile in
(5) is at most \(B_*\); the constant \(E_*<69/100\) is also
less than \(B_*\). Thus \(\mathcal A(c)\le B_*\).
The original action calibration, equations (7) and (17), yields
\[
 \mathcal A(c)+\Re\Theta(a_c,b)-\tfrac12\Re g(b)
 \le\Lambda(z)-(\kappa+\kappa_R)(1/2-a_0)^2
                         -\kappa_R(z-b_0)^2 ,
 \quad\kappa_R=8\kappa/9 .
 \tag{24}
\]
Its gap is greater than \(\delta_R\).

The physical-row proof, before finite summation, pays every
regular cap profile against every \(t\in[0,2/25]\cup[1/2,1]\)
at this endpoint with gap \(2\delta_R\) and the original
\(-\kappa(z-b_0)^2\) term. Its formal true-end comparison
uses \(C=3/5\) and has the additional reserve \(29/200\)
at the half face, by equation (10) of that proof. Replacing \(C\)
by \(E_*\) costs less than \(9/100\), leaving \(11/200\).
Consequently
\[
 \mathcal A(c)+E_c(t)-\tfrac12\Re g(b)
 \le\Lambda(z)-\kappa(z-b_0)^2-2\delta_R
            \quad(t\in[0,2/25]\cup[1/2,1]).
 \tag{25}
\]
This uses the individual calibrated profiles, not the modulus
of a signed complete product.

At \(h=H\), \(\mathcal A(H)\) is exactly the half-face cap
envelope used in Sections 2 and 5 of the selected upper-right
theorem. Its original profile proof gives
\[
 \mathcal A(H)+
 \max\left\{\Re\Theta(a_H,b),
             \max_{t\in[0,2/25]\cup[1/2,1]}E_H(t)\right\}
       -\tfrac12\Re g(b)
 \le\Lambda(z)-\gamma_0,\qquad\gamma_0=1/4000 .
 \tag{26}
\]
The low extension to \(2/25\), critical-height calibration, high
physical rows and separate true-end reserve are all included in
that cited profile statement.

Since \(\delta_R<\kappa<\gamma_0\), convex interpolation of
(24)--(26) pays the critical and each low profile for every
\(c\le h\le H\). Equations (20)--(22) pay the high profiles
by the appropriate endpoint. Therefore
\[
 \mathcal A(h)+
 \max\left\{\Re\Theta(a_h,b),
             \max_{t\in[0,2/25]\cup[1/2,1]}E_h(t)\right\}
       -\tfrac12\Re g(b)
 \le\Lambda(z)-\delta_R .
 \tag{27}
\]
In particular this holds separately for each profile in (5)
and for \(E_*\), including at height zero.

One additional cap reserve survives pointwise on the whole height
interval. For fixed \(u\in[.27,.49]\), the regular strip argument
\[
 \mathcal B(u,\eta+h)
  =\Arg(1-e^{2\pi(\eta+h)-2\pi i(1/2+u)})
\]
decreases as \(h\) increases. Its derivative has the sign of
\(\sin(2\pi(1/2+u))<0\). In the exact canonical identity
\(\Im\Psi_e=\mathcal B+T(e)\), the second term is independent
of \(h\). Thus every lower bound for \(\Im\Psi_e\) used in
equations (19)--(20) of the selected half-face theorem at \(H\)
is at least as strong at \(h\le H\). Integrating from the
unchanged actual \(h_e\) to \(.04\) gives, at the same \(u\),
\[
 \Re\Psi(u+.04i,a_h)-.08\pi
 <\Re\Psi(u+ih_e,a_h)-\frac{437\pi}{50000}
 <\Re\Psi(u+ih_e,a_h)-\frac1{50}.
 \tag{27a}
\]
Consequently the upper cap alias paired with any critical or
physical profile in (27) has the additional reserve \(1/50\).
In particular it retains that reserve at the real half face.

## 6. Complete finite conclusion and the stronger real true-end bound

Proposition 2 of the selected upper-right theorem bounds the
whole \(C_{1,N}\) by exactly the maximum in (27), with any
prescribed rate allowance. Its literal decomposition includes
both full physical end blocks, the entire critical-height line,
both unweighted connecting sides, all four weighted vertical
half-sides, and both horizontal aliases. The latter can be
suppressed at one sufficiently tall fixed height uniformly on
the compact parameter interval. In particular no contribution
is discarded because only the critical action has a favorable
height comparison.

Multiply that complete bound by (7), the two original first
Fourier alternatives and the outgoing halfweight. Equation (27)
pays every term. Uniform symbol errors, finite row counts,
half-grid displacements and exact residue factors can be shared
within \(\delta_R/2\), or included in the requested allowance.
This proves (4). All contours and heights are fixed before \(N\);
both original parity-dependent cuts remain in the conditional
source. The literal degree in \(w\) is less than \(N\).
Continuation from the full real interval by the original
Chebyshev argument adds an arbitrarily small fixed rate
allowance on a fixed ellipse, and Cauchy estimates supply fixed
derivatives on smaller disks. The halfweight is a constant
multiplier in this argument and is never divided out.

**Corollary 2 (individual real-face profiles).** At \(a=1/2\),
each of the five cap profiles and the constant \(E_*\), paired
with the critical conditional action or any physical end/cut
rate \(E_0(t)\), has the bound \(\Lambda(z)-\delta_R\) in
(27), with the unchanged outgoing halfweight. Both unselected
and selected first Fourier upper rates are zero at this face.

The genuine cap true-end groups on \(|X|=1\) also admit the
smaller constant \(C=3/5\). For this constant the stronger
profile bounds are
\[
\begin{split}
 C+\Re\Theta(1/2,b)-\tfrac12\Re g(b)
 &<\Lambda(z)-(\kappa+\kappa_R)(1/2-a_0)^2
            -\kappa_R(z-b_0)^2-\frac{29}{200},\\
 C+E_0(t)-\tfrac12\Re g(b)
 &<\Lambda(z)-\kappa(z-b_0)^2-2\delta_R-\frac{29}{200},
            \qquad t\in[0,2/25]\cup[1/2,1].
\end{split}
\tag{28}
\]
For the first inequality use \(B_*-C>29/200\) at \(h=c\),
the original critical comparison, and (17). For the second
use the formal constant comparison at the negative half face
and (20), (23). Thus the larger reserve is retained without
interpolating two different Fourier alternatives.

The original geometric constant and marginal have not been
recalibrated. The statements end on the real half face. A real
continuation, any right arc, the remainder of the first period,
and departures of later coordinates are not asserted here.

## Direct source versions

| Source | SHA-256 |
|---|---|
| research_mixed_selected44_upper_right_complete_pair.md | aee07a0914def14645fe344173883de690a2e0c4591ee65ce7873ce6627515d7 |
| research_mixed_selected44_right_half_interval.md | 50d7d9daaf5e33f45749b7c5ca9e2dba4fd0dca2298986d337cb58e35979ebc1 |
| research_mixed_initial44_lower_right_action_calibration.md | ef0079ed2c3148db13a24c23e715d9daab6e164b1aff0231de11041613e0106f |
| research_mixed_initial44_lower_right_physical_rows.md | 6665075b979801c0d5b9296738508be527bddd8827e3aea004b9ff1e7a60f702 |
| research_mixed_first_four_cap_lower_right_horizontal.md | 4d41a967edabf0710fc7b04b723bb3e2fb7a407d44bb5a0fc1678e3f9ee5ee6e |
| research_mixed_cap_upper_target_extension.md | c705f72cbfaac8dc920ce48a4f6ea0402f15449f3ba4af202a04c5015cf2d46e |
| research_mixed_cap_upper_target_completion.md | 49292f204a86e08c48c5aa8fd29f98103f38a939bb88d523afdd8be741650c22 |
| research_mixed_conditional_lower_output_middle_reduction.md | 9df0e7cdf4a193783e236e8e0fa8f416b5a123d8afe02033601be333cf6d5bc7 |
| research_mixed_four_conditional_positive_incoming_action.md | e8608019efbd73b2c05e6ede084b4781182259dc0e32be12b4610c66f352d371 |
| research_mixed_boundary_window_real_color_envelopes.md | 727aa6b7b477e3a984da4241d3ac9356858553e8aae74752bcf930a74abecd4b |
| research_mixed_fourier_weight_continuation.md | 0bae41d83f414eb91fd137de1242120a11408147d56ec752e466ca5ed7e7f48e |
| research_mixed_horizontal_complex_extension.md | c7837a9dfb072f2e276f5ccdb99c7421e154a4ca073a078540d8064dbb3747d4 |

The whole written proof and its directly used source implications
were read in full; all twelve source bindings were checked. Independent
review is required before adoption.
No mathematical numerical evaluation, saved-value arithmetic, test,
import, compilation or frozen-source edit is used.
