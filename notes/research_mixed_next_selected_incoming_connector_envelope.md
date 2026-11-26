# A complete source envelope on the selected incoming connector

Research deduction, 7 November 2026. The original incoming vertical
connector admits an upper envelope interpolating its already paid
negative-height endpoint and an explicit real-half-face envelope.
This is a statement about the complete finite source, with its
physical rows and contour currents. It does not assert that the
real-half-face envelope is below the following affine action.
No numerical evaluation, replay, or new saved comparison is used.

## 1. The actual connector and the endpoint envelopes

Retain exactly the ordinary-next canonical family and normalization of
[the selected incoming right-segment theorem](research_mixed_second_selected_first_three_right_segment.md),
Sections 1--2:
\[
 (a_*,u_*,z_*,v_*,b_*)=(r_1,s_2^*,r_2,s_3^*,r_3),
 \qquad(\epsilon_1,\epsilon_2,\epsilon_3)=(0,1,\beta),
 \qquad\beta\in\{0,1\}.                                      \tag{1}
\]
Both indices \(u_*,v_*\) are ordinary. The external parameter remains
the same \(s_4^*\in K_3\cup K_4\); no terminal graph replaces this
reference. In particular
\[
 -\frac9{125}<h_a:=\Im a_*<0,\qquad
 -\frac{51}{500}<h_u:=\Im u_*<0.                              \tag{2}
\]
The strict negative incoming height is an actual-family consequence
of the proved following-prefix geometric guards, not of independently
varying containing boxes.

Put
\[
 \begin{gathered}
 P=[11/50,9/20],\quad H=1/100,\quad z=y+iH,\quad
 b=w+i\Im b_*,\quad y,w\in P,\\
 a_\theta=\frac12+i(1-\theta)h_a,\quad 0\le\theta\le1,\qquad
 X_\theta=e^{-2\pi ia_\theta},\quad
 Y=e^{-2\pi iz},\quad Z=e^{-2\pi ib}.
 \end{gathered}                                               \tag{3}
\]
Thus the connector is the original oriented segment from
\(1/2+ih_a\) to \(1/2\). If its exact decomposition first passes
through the original pair height, the two adjoining segments
concatenate to this one, with any overlapping portions cancelling
with their original orientations. No real arc replaces it.

The nonnegative complete density is
\[
 \mathcal B_N(\theta)=
 |U_{0,N}(\omega,X_\theta)C_{1,N}(X_\theta,Y)
   d_N(Y)Y^{-N}C_{\beta,N}(Y,Z)|\,|d_N(Z)|^{\beta/2}.            \tag{4}
\]
There is no incoming Fourier halfweight. At \(\beta=0\) the
last factor is identically one, including at zeros of \(d_N\).
All finite factors are the original ones.

Use the original affine target \(\Lambda_{123}(b)\) in
equation (4) of the right-segment theorem. Its proof supplies the
sourcewise endpoint ceiling
\[
                 L_-(b)=\Lambda_{123}(b)-\frac1{400}.          \tag{5}
\]
For the other endpoint, define the real conditional profile
\[
 \begin{split}
 Q(t;a,z)&=g(a+t)+g(z+t)-3g(t)-g(a)-g(z)+2\pi iat,\\
 \overline q_H(y)&=\max_{0\le t\le1/2}\Re Q(t;1/2,y+iH),\\
 H_0(y)&=\max\{-J(y)/2-3\pi/400,0\},\\
 L_+(y,b)&=M_{\rm half}+\overline q_H(y)
                         +H_0(y)+B_3(y,w)+7/250 .
 \end{split}                                                  \tag{6}
\]
The continuous value is used at the numerator endpoint \(t=1/2\).
Here \(M_{\rm half}\) is the original complete cap action in
[the whole half-cap theorem](research_mixed_half_face_complete_cap_packet.md),
and \(B_3\) is the original ordinary third-factor supporting plane
from [the full selected-plateau comparison](research_mixed_next_filtered_selected_plateau.md),
Section 4. Its quadratic losses and original outgoing marginal
are retained. Neither \(M_{\rm half}\) nor \(B_3\) has a new
additive normalization.

**Theorem.** For every prescribed \(\tau>0\), uniformly on (1)--(3),
all real ordinary colors \(\omega\in[-2,2]\), both parities, and all
sufficiently large \(N\),
\[
 \boxed{\quad
 \mathcal B_N(\theta)\le C_\tau N^{A_\tau}
       \exp N\{(1-\theta)L_-(b)+\theta L_+(y,b)+\tau\}.
 \quad}                                                       \tag{7}
\]
The same upper rate holds for fixed ordinary-color derivatives,
with polynomial factors. On sufficiently small fixed neighborhoods
of complete color it holds with the prescribed tolerance.
The finite source and all its fixed outside-variable derivatives
also have the corresponding local upper estimate as described in
Section 6. No modulus halfweight is differentiated.

In particular (7) is bounded by the larger of the two endpoint
exponents. Replacing \(M_{\rm half}\) in (6) by the proved upper
bound
\[
             \widehat M=\frac{203}{200}
                                  -\frac{1303}{7680000}        \tag{8}
\]
is permissible. A strict comparison of (6), or of this enlarged
version, with \(\Lambda_{123}\) is a separate requirement.

## 2. One common finite contour atlas

Write \(r=e^{-2\pi i/N}\), \(P_j=(r;r)_j\), and
\(p_j(X)=(rX;r)_j\). The literal first two factors remain
\[
 \begin{split}
 U_{0,N}(\omega,X)&=\sum_{j=0}^{N-1}
                    H_N(\omega,r^{-j})\,p_j(X)/P_j,\\
 C_{1,N}(X,Y)&=\sum_{j=0}^{N-1}
                    X^{-j}p_j(X)p_j(Y)/P_j^3 .
 \end{split}                                                  \tag{9}
\]
The endpoint coefficient in the cap is complete and coherent.

For the cap use the original real cuts \(27/100,49/100\), the
horizontal alias heights \(-11/200,1/25\), and the exact density
\[
 \mathscr A_N(e,a,\omega)=
 D_N(e)^{-1}C_N(e,\omega)\frac{\Pi_N(a+e)}{\Pi_N(a)}.            \tag{10}
\]
Let \(h_e\) be its actual original private critical height and
let \(h_{\rm half}=\Im e_+\) be the half-cap critical height.
Choose the main height
\[
            \eta_e(\theta)=(1-\theta)h_e+\theta h_{\rm half}.
                                                                    \tag{11}
\]
Both endpoints, and hence the whole interpolation, lie in
\(E_c=[.27,.49]+i[-.055,.04]\). The five cap profiles are its
main line, its two real cuts, and its two horizontal aliases
with penalties \(11\pi/100,2\pi/25\).

[Upper-target cap extension, Theorem 2](research_mixed_cap_upper_target_extension.md)
supplies this complete five-profile envelope throughout
\[
             \Re a=1/2,\qquad -9/125\le\Im a\le0.             \tag{12}
\]
Its proof, before summing, reduces every compact physical private
tail to those same real cuts, includes all revived rows, and
retains the zero-mode joins and both sign halves of the vertical
aliases. It permits any intermediate main height in \(E_c\).
Thus (11) changes no physical support or endpoint coefficient.

The true private ends are treated separately. Use the actual
negative-height bound in
[complete upper-target support, Section 3](research_mixed_cap_upper_target_completion.md),
not the unnecessarily rounded \(3/4\) in the envelope statement.
The lower end is below \(1/4\), and the upper end has rate at most
\[
       \frac35+\frac1{100}\log(40/19)<\frac{37}{50}.            \tag{13}
\]
This holds uniformly in (12); the positive-height term is zero.
The bottom cap plane exceeds \(149/200\), and
\(M_{\rm half}>47/50\), so the extra constant profile \(37/50\)
fits both cap endpoint bounds. This retains the true endpoints
without extending a compact coefficient packet to zero or one.

For \(C_1\), keep the common real cuts
\[
 \ell=3/40,\qquad
 L_N=\lceil3N/40\rceil,\quad M_N=\lceil N/2\rceil,\quad
 t_-=(L_N-1/2)/N,\quad t_+=(M_N-1/2)/N,                       \tag{14}
\]
and main height
\[
                       \eta_t(\theta)=(1-\theta)h_u .         \tag{15}
\]
The horizontal aliases stay at heights \(-1/5,5/4\). The exact
retained-row interpolant is
\[
 \mathscr T_N(t;a,z)=e^{2\pi iNat}
  \frac{\Pi_N(a+t)\Pi_N(z+t)}
       {\Pi_N(a)\Pi_N(z)\Pi_N(t)^3}.                          \tag{16}
\]
At \(t=j/N\) it is exactly the second summand in (9), with no
additional diagonal or normalization. Apply the original finite
rectangle identity only to \(L_N\le j<M_N\). Its constant
residue density is \(+N\); the main, two horizontal aliases,
four vertical aliases, and two unweighted joins all remain.
The rows \(j<L_N\) and \(j\ge M_N\) remain literal products.

Every reciprocal argument in (10), (16) is regular. At odd \(N\),
\(t_+=1/2\), so the numerator \(a+t\) can equal one. It is
retained as a numerator, with its original zero-safe continuation.
Section 3 below handles the corresponding rate explicitly;
no regular-strip Hessian is applied through that divisor.

## 3. Joint height convexity, including the numerator corner

At complete color the cap phase is
\[
           \Psi(e,a)=S(e)+J(e+a)-J(a)-i\pi ea.                \tag{17}
\]
Write \(C(s)=\Re\cot\pi s\). At \(\Re a=1/2\), one has
\(C(a)=0\), at every height. Put
\[
 s_e=-\Re S''(e)/\pi>0,\quad b_e=-C(a+e)>0,\quad
 b_t=-C(a+t)>0,\quad c_t=3C(t)-C(t+z).                       \tag{18}
\]
On \(E_c\), the first assertion follows from the original endpoint
rectangle, as used in the upper-target extension. For
\(3/50\le\Re t<1/2\), every bounded index height and selected \(z\),
Lemma 2 of
[the complete real-arc conditional theorem](research_mixed_real_arc_complete_conditional_packet.md)
in fact proves \(c_t>0\), independently of the incoming height:
if \(\Re(t+z)\ge1/2\) the shifted cotangent is nonpositive;
otherwise its proof gives
\[
                    C(t+z)/C(t)<1792/615<3.                 \tag{19}
\]
The real part of \(a+t\) lies in \((1/2,1)\), proving the sign
of \(b_t\).

The negative real Hessian of \(\Psi+Q\), divided by \(\pi\),
has the exact real quadratic form
\[
 s_e\,de^2+c_t\,dt^2
                  +b_e(de+da)^2+b_t(dt+da)^2.                \tag{20}
\]
The chirps contribute only imaginary Hessian entries.
Consequently the real rate is convex along every affine
interpolation of the three imaginary heights, with real
private/index coordinates fixed. The same is true when one
of the heights is constant. Fixed alias penalties are constant
in \(\theta\), so do not change this assertion.
If the cap's constant true-end profile (13) is used instead,
the last two-variable part of (20) gives the required convexity.

For completeness, the conditional face at \(\Re t=1/2\)
is not a regular instance of (20). The original continuation
has the exact continuous real rate
\[
                    \Re g(1+i\xi)=\pi\max(\xi,0).            \tag{21}
\]
Its derivative jumps upward. For \(\Re t<1/2\) the preceding
convexity is valid; passage to the continuous closed-face rate,
or direct use of (21), preserves convexity. The finite numerator
zero in (16) is not removed. At even levels \(t_+<1/2\);
at odd levels (21) supplies precisely the necessary limiting
bound. This is the same zero-safe face treatment as equation
(24) and its preceding paragraph in the selected right-segment
proof.

## 4. Reduction of every conditional current and physical row

The unchanged original-log argument estimate on this atlas is
\[
       -7\pi/4<\Im Q_t<141\pi/100,\qquad
                3/40\le\Re t\le1/2,                         \tag{22}
\]
for every finite index height. Its proof is equation (22)
of the right-segment theorem: it uses only the real parts,
\(\Re(a+t)\ge23/40\), and the original strips. In particular
it does not assume \(\Im a=h_a\).
With (2), (15), the two weighted horizontal aliases lose at
least the constants \(59\pi/500,67\pi/500\) in that theorem's
equation (23), relative to the main profile. Moving the main
height toward zero only improves the latter upper-alias
allowance. Both vertical aliases are monotone toward their
zero-height endpoints, by (22) and their exact penalties.
Each unweighted join is bounded by its two endpoints using
height convexity; at the upper cut use (21).

It follows that all nine retained currents are bounded by
the maximum of the main profile and the two real-cut profiles,
with the original polynomial costs. No signed whole-conditional
bound is used to estimate a constituent current.

The lower physical rows are also covered. At real
\(0<t\le3/40\), the exact force, including the chirp, has
incoming modulus at least one, outgoing modulus greater than
\(9/10\), and own denominator smaller than \((4/5)^3\).
Thus the real rate increases to the lower cut, uniformly for
every incoming height in (12). It extends continuously to
the literal row \(j=0\). Alternatively each such row has
incoming-height convex rate, with both endpoint rates paid;
no complex-index continuation at zero is needed.

For all upper rows invoke
[the high-row endpoint theorem, Lemma 1](research_mixed_transformed_upper_rows.md).
Its stated domain includes \(\Re a=1/2,\Re z\in P\),
\(|\Im a|<.072,|\Im z|=.01\). The complete positive sum of
all \(j\ge\lceil N/2\rceil\), including every revived row,
is bounded by the half and last rate
\[
 \begin{split}
 R_{\rm half}(h,z)
       &=\Re Q(1/2;1/2,z)-\pi h,\\
 R_{\rm last}(h,z)&=2\pi H-2\pi h,\qquad h\le0 .              \tag{23}
 \end{split}
\]
Indeed the incoming half-period integral of
\(\log|1+e^{2\pi h}e^{-2\pi iu}|\) is zero for \(h\le0\);
the full-period means are zero for the incoming factor and
\(2\pi H\) for the outgoing one. The remaining terms in
(23) are exactly the original chirp. Both rates are affine
in \(h\), and hence can be interpolated with every cap profile.
This argument is a complete high-row bound, not a triangular
physical-support assertion.

At \(\theta=1\), the main, both real cuts, and the half rate
are at most \(\overline q_H(y)\). The last rate is \(2\pi H\),
also strictly smaller than \(\overline q_H(y)\). To see this,
the complete real-arc conditional theorem proves its critical
action \(>13/24\); vertical convexity at the critical real
coordinate puts that action below its real profile maximum.
Finally \(2\pi/100<13/24\). Thus every conditional source
profile at the top has the upper bound in (6).

## 5. Endpoint calibration and complete assembly

At \(\theta=0\), all five cap profiles lie below the original
whole-cap plane
\[
 B_U(1/2)=\Re T_0(a_*)-\Re p_L(1/2-\Re a_*)
                             -\kappa_*(1/2-\Re a_*)^2.       \tag{24}
\]
This is a sourcewise assertion of complete upper-target support,
not a conclusion obtained from the modulus of the signed cap.
Its true-end profile (13) lies below the same plane.
The conditional main height is \(h_u\), and its lower cut is
exactly the endpoint \(3/40\) of the moving cut in the
right-segment theorem. That theorem pays, with the common
raw loss \(1/400\), every combination of:

* the first conditional main, lower real cut, half and last profiles;
* every original third-factor profile, physical tail and current;
* each of the two original full selected-weight alternatives.

Its Sections 3 and 5 reduce the first half and last profiles to
the first main profile pointwise. Its Section 4 separately pays
the third-factor last profile. Section 6 keeps the actual cap
plane (24) and its marginal cancellation. Thus (5) is valid
for every source combination used here before summing.

At \(\theta=1\), the whole half-cap proof bounds each of the
same five cap profiles by \(M_{\rm half}\), using the original
\(.27,.49\) cuts and alias heights. The constant true-end
profile is smaller by (13). Section 4 bounds every first
conditional profile by \(\overline q_H(y)\).

To make the remaining allocation explicit, retain the two
selected halfweight rates
\[
 \eta_{\rm fac}(z)=\tfrac12[-\Re g(z)-2\pi H],\qquad
                       \eta_{\rm force}(z)=0.               \tag{25}
\]
For either full-weight alternative, use the same alternative
on its two halves; no division at a zero of \(d_N\) occurs.
The original third-factor source comparison gives each of
its allocated profiles, with its first half of (25) and its
original outgoing halfweight, the bound
\[
                         B_3(y,w)+7/250 .                   \tag{26}
\]
This follows before summing from the current-by-current proof
of equation (22) in
[the full-plateau target theorem](research_mixed_first_collar_full_plateau_second_target.md),
Section 4, as used in equation (17) of the filtered selected
plateau theorem. The remaining half satisfies
\(\eta_{\rm fac},\eta_{\rm force}\le H_0(y)\). Both outgoing
Fourier alternatives, if present, remain in (26).
Thus the top bound for every same source combination is
exactly \(L_+\) in (6).

For fixed real private/index coordinates and each fixed source
label, the only varying rates are the cap and first conditional
ones. Their sum is convex in \(\theta\), by (20)--(23).
The third profiles and selected weights are independent of
\(\theta\). Each such combined rate is therefore at most
\[
                       (1-\theta)L_-+\theta L_+.            \tag{27}
\]
Taking maxima over the fixed coordinates and labels preserves
this bound. The physical cap tails have already been reduced
to this same cap atlas by the full envelope theorem; the
conditional lower and upper pieces were retained in Section 4.
All exact residue densities remain \(+N\), and all finite
row counts and current lengths cost only polynomial factors.

Use the original half-grid private cuts converging to
\(.27,.49\) and the cuts (14). Their \(O(N^{-1})\) shifts
are absorbed in one prescribed tolerance by the uniform
continuous upper rates, including (21). The zero-safe
factorial-product bounds retain actual numerator zeros and
their \(O(\log N)\) errors. This proves (7) at both parities.

## 6. Colors, local derivatives, and what is not concluded

On the complete retained cap rectangle the original all-real
endpoint coefficient theorem bounds each whole \(C_N(e,\omega)\)
by its complete-color rate, with its established angular loss.
The compact physical cap tails and true ends have their
separate all-real bounds. Therefore all preceding upper
comparisons hold uniformly on \([-2,2]\), without assigning a
remote real-color critical point. Whole-interval Markov bounds
give each fixed ordinary-color derivative of the literal
polynomial with a polynomial loss, before any strict reserve
is allocated.

For small complex color neighborhoods, the same exact source
estimates incur an arbitrarily small prescribed rate allowance.
At each fixed base connector and outside parameter, keep its
cuts, reference heights, and contour labels fixed when taking
derivatives. The reciprocal factors stay in their compact
regular charts. The possible numerator zero is controlled
by its continuous zero-safe upper product rate, including in
small complex neighborhoods; no reciprocal of it is introduced.
The physical high-row rate is continuous on the compact
parameter/index set, so its endpoint upper comparison on
the base set persists with the same small allowance even
though a perturbed real part need not remain in the exact
domain of the high-row endpoint lemma. True-end polynomial
bounds have the same small-radius allowance. Compactness
then supplies fixed neighborhoods and Cauchy estimates for
all fixed derivatives of the literal integer-weighted source.
The outgoing modulus halfweight is kept external to these
derivatives.

The exact local joint packet is compatible with this upper
bound, but is not used to cover a macroscopic vertical segment.
Equation (7) is a complete connector endpoint-envelope theorem.
It proves a strict connector gap whenever both endpoint
envelopes have a uniform strict gap; it does not supply the
missing sign of \(L_+-\Lambda_{123}\). In particular no
inconclusive saved comparison is promoted to a positive
certificate. The other retained-variable contour pieces and
the whole selected Fourier sector are not estimated by (7).
