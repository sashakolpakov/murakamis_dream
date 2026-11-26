# The signed first-four/three negative-height connection

Private written proof, 10 November 2026. The first retained coordinate
can move from its actual negative height to zero at real part one
tenth, while the next coordinate stays at its actual height. The
wrapped ordinary block is retained as a signed finite sum. Its two
wall rates, together with the other unchanged source profiles, give
a convex upper envelope on this vertical interval. No absolute-row
envelope is asserted inside the wrapped block.

## 1. Actual reference, source and rate

Fix an actual positive three/four open word of length \(m\ge3\)
beginning with four and three. Keep its original reference, lifts
and normalization:
\[
 a_*=a_0+ic,\quad b_*=b_0+id,\quad
 e_*=u_*+ih_e,\quad s_*=v_*+ih_s.
\]
The [complete actual-height pair](research_mixed_early_four_three_complete_pair.md)
and equation (1) of the
[selected finite-source reduction](research_mixed_selected_four_three_finite_reduction.md)
give
\[
 .246<a_0<.350,\qquad -.070<c<-.020,\qquad
 -.051<h_e<-.019,\qquad -.065<h_s,d<.068.
\tag{1}
\]
The sharper private-height interval in (1) is the actual ordinary
type-three image in that finite reduction. The larger interval
\([-.108,.068]\) in the complete-pair statement is only a containing
bound; no new reference or private height is chosen here.
Set
\[
 x=\frac1{10},\quad a=x+ih,\quad c\le h\le0,\qquad
 b=z+id,\quad z\in P=[11/50,9/20].
\tag{2}
\]
These are targets at the unchanged coupled reference, not independent
points of the boxes in (1).

With \(q_N=e^{-2\pi i/N}\), \(P_j=(q_N;q_N)_j\),
\(p_j(X)=(q_NX;q_N)_j\), \(X=e^{-2\pi ia}\) and
\(Y=e^{-2\pi ib}\), retain literally
\[
\begin{split}
 U_{1,N}(w,X)&=\sum_{i=0}^{N-1}
       \frac{H_N(w,q_N^{-i})p_i(X)}{P_i^2},\\
 R_{j,N}(a,b)&=X^{-j}\frac{p_j(X)p_j(Y)}{P_j^2},
 \qquad C_{0,N}(X,Y)=\sum_{j=0}^{N-1}R_{j,N}(a,b),\\
 \mathcal K_N^0(w;a,b)&=U_{1,N}(w,X)C_{0,N}(X,Y)d_N(X).
\end{split}
\tag{3}
\]
The cap coefficient is complete, the whole first Fourier polynomial
is present, and no selected monomial occurs in (3). There is no
outgoing type-three halfweight. No external scalar is changed.

Use the original bare phases
\[
\begin{split}
 \Psi(e,a)&=S(e)+g(e+a)-g(a)-g(e)
                         -\frac{i\pi}{2}(e-e^2),\\
 Q(s;a,b)&=g(s+a)+g(s+b)-2g(s)-g(a)-g(b)+2\pi ias,\\
 \mathcal F(e,s;a,b)&=\Psi(e,a)+Q(s;a,b)-g(a).
\end{split}
\tag{4}
\]
Here \(g=J+i\pi(t-t^2)/2\), \(J'(t)=\operatorname{Log}(2\sin\pi t)\), \(J(0)=0\),
and \(S\) is the same complete-end action. In the allocations of the
complete-pair source, \(\Xi_1=\Psi-g(a)/2\) and
\(F_{10}=Q-g(a)/2\); their sum is (4). Put
\[
\begin{split}
 M&=\Re\mathcal F(e_*,s_*;a_*,b_*),\qquad
 p=\mathcal F_b(e_*,s_*;a_*,b_*),\\
 \Lambda(z)&=M+\Re p\,(z-b_0),\qquad
 \Gamma(z)=\Lambda(z)-\kappa(z-b_0)^2,\qquad
 \kappa=1/2500000,\\
 \gamma_*&=\kappa(a_0-11/50)^2,\qquad
 \gamma_{43}=\min\{\kappa,\nu/4\}(a_0-11/50)^2.
\end{split}
\tag{5}
\]
The uniform \(\nu>0\) is the original Schur constant in the
[positive-private-height central source](research_mixed_early_four_three_positive_private_central.md).
Thus \(0<\gamma_{43}\le\gamma_*<1/2000\), uniformly away from zero
on the actual family. The critical first-coordinate marginals cancel
in precisely this normalization.

**Theorem 1.** For every \(\tau>0\), both parities and every real
ordinary color \(w\in[-2,2]\),
\[
 |\mathcal K_N^0(w;a,b)|
 \le C_\tau N^{A_\tau}
       \exp N\{\Lambda(z)-\gamma_{43}+\tau\}
\tag{6}
\]
uniformly on (2), for all integers \(N\ge2\).
It also holds on a sufficiently small fixed ordinary-color disk
about \(-2\), with any prescribed total rate allowance and fixed
derivatives on smaller disks. The same bound pays the literal
oriented first-coordinate integral on this segment with the
original outside scalar. The stronger interpolated rate is (21)
below.

## 2. A common envelope which preserves the signed block

Let \(A(h)\) be the maximum of the five bare cap profiles
\[
\begin{array}{ll}
 \displaystyle\max_{.27\le u\le.49}\Re\Psi(u+ih_e,a),&
 \Re\Psi(.27,a),\quad\Re\Psi(.49,a),\\
 \displaystyle\max_{.27\le u\le.49}\Re\Psi(u-.055i,a)-.11\pi,&
 \displaystyle\max_{.27\le u\le.49}\Re\Psi(u+.04i,a)-.08\pi,
\end{array}
\]
and the separate true-end ceiling
\[
                         A_*(h)=3/5+\log4/100.
\tag{7}
\]
The [independent-height full cap theorem](research_mixed_cap_early_fixed_height_full_source.md),
Theorem 2, supplies exactly these profiles on (2). Its type-four
upper-row allowance is zero, and its general end ceiling
\(3/5+2\pi h_++\log4/100\) is constant here. All cap currents,
physical tails and true ends are included.

Let \(\mathscr C_0\) be the following compact ordinary inventory,
where \(v\in[3/20,1/2]\):

| Piece | Private point \(s\) | Penalty \(\omega\) |
|---|---|---|
| Main zero mode | \(v+ih_s\) | \(0\) |
| Both zero-mode joins | \(\ell+iy\), \(\ell\in\{3/20,1/2\}\), \(y\) between \(0,h_s\) | \(0\) |
| Lower horizontal alias | \(v-i/5\) | \(2\pi/5\) |
| Upper horizontal alias | \(v+i/5\) | \(2\pi/5\) |
| Four vertical alias halves | \(\ell+iy\), \(\ell\in\{3/20,1/2\}\), \(y\in[-1/5,0]\cup[0,1/5]\) | \(2\pi|y|\) |

The real cuts occur at \(y=0\). Retain the full physical rate
\[
\begin{split}
 E(t;a,b)={}&\int_0^t\log|1-e^{-2\pi i(a+v)}|\,dv
       +\int_0^t\log|1-e^{-2\pi i(b+v)}|\,dv\\
       &-2J(t)-2\pi ht.
\end{split}
\tag{8}
\]
It is continuous through its integrated logarithmic zeros. Its
complete endpoint carrier is
\[
                         E(1;a,b)=2\pi(-h+d_+).
\tag{9}
\]
Define
\[
\begin{split}
 B(h,b)=\max\bigg\{&
 \sup_{(s,\omega)\in\mathscr C_0}\{\Re Q(s;a,b)-\omega\},
 \sup_{1/2\le t\le1-z}E(t;a,b),\\
 &E(1-z;a,b),\ E(1-x;a,b),\ 2\pi(-h+d_+)\bigg\},\\
 W_0(h)&=\max\{-\Re g(a),0\},\qquad
 \mathcal E(h,b)=A(h)+B(h,b)+W_0(h).
\end{split}
\tag{10}
\]
The repeated first wall in (10) makes the two signed-block
boundary rates explicit. No interior rate with \(1-z<t<1-x\)
occurs in this envelope.

For every \(\tau>0\), the exact full source satisfies
\[
 |\mathcal K_N^0(w;a,b)|
       \le C_\tau N^{A_\tau}e^{N\{\mathcal E(h,b)+\tau\}}.
\tag{11}
\]
We give the finite-source justification before proving its sign.
Split the ordinary indices into the exact low, central and high
blocks
\[
 j\le\lfloor3N/20\rfloor,\qquad
 \lfloor3N/20\rfloor<j<\lceil N/2\rceil,\qquad
 \lceil N/2\rceil\le j<N.
\tag{12}
\]
The [low-row ratio](research_mixed_first_attached_low_row_transport.md),
Lemma 1, exceeds \(e^{1/200}\) on the independent height box
containing (2), through \(N/5\). The low block is at most 201 times
its final row, whose continuous rate tends to \(\Re Q(3/20;a,b)\).
Its rounding tolerance and the original zero-safe estimate are
uniform, including \(j=0\).

For the central block use the original factorial interpolation
at half-grid cuts tending to \(3/20,1/2\), with heights \(\pm1/5\).
All factorial real arguments are in fixed compact subintervals
of the original strip; in particular
\(\Re(s+a)\in[.25,.6]\) and \(\Re(s+b)\in[.37,.95]\).
The exact residue identity therefore keeps the original positive
zero-mode density \(+N\). Moving only that zero mode to \(h_s\)
leaves both joins, both horizontal aliases and all four vertical
halves in \(\mathscr C_0\), with the displayed penalties.
The [exact factorial theorem](exact_factorial_interpolation_and_complex_contours.md)
allows this fixed imaginary-height compact set. Nothing in this
construction requires a new critical point at the intermediate
first height.

Partition the high indices disjointly into
\[
\begin{array}{ll}
 I_U:&j/N\le1-z,\quad j/N<1-x,\\
 I_W:&1-z<j/N<1-x,\\
 I_L:&j/N\ge1-x .
\end{array}
\tag{13}
\]
The [zero-safe physical-product bound](research_mixed_conditional_contour_allowance.md),
Section 2, pays the absolute sum on
\(I_U\) by the unwrapped supremum in (10). The
[reflection lemma](research_mixed_right_tail_reflection.md),
Lemma 1, applies since \(0\le1-t\le x\le z\le1/2\) on \(I_L\);
its proof only uses these inequalities. It gives
\[
 E(1-v)-E(1)\le-2\pi(-h+d_+)v\le0,\qquad0\le v\le x.
\tag{14}
\]
Thus the absolute late sum is paid by (9), including the literal
last index and any wall row.

For \(I_W\), apply Theorem 1 of the
[signed one-wall source](research_mixed_negative_height_wrapped_contour.md).
Its full independent domain includes \(c\le h\le0\) in (2).
It bounds this signed sum by
\(\max\{E(1-z),E(1-x)\}\), with arbitrary prescribed tolerance.
In particular its exact physical identity
\[
 R_{j,N}=(1-Y^N)F_N(j/N)
\]
is used without division. The original two Fourier terms of the
off-grid identity, all wall collars and all finite contour corrections
remain included. The multiplier has precisely rate \(2\pi d_+\),
already present in (8), not an additional debit. If it vanishes,
the strict wrapped block is zero. The triangle inequality is used
only between the three whole blocks in (13), never between the
rows of \(I_W\).

The complete cap theorem and the full Fourier upper bound now give
(11). Since \(h\le0\), that Fourier bound is exactly \(W_0\);
its forcing branch is retained. All finitely many symbol, length
and rounding allowances fit inside one \(\tau\), uniformly in both
parities. Small levels can be absorbed in the constant.

## 3. Convexity in the first height

For \(|h|\le39/500\), put
\[
 C_a(h)=\Re\cot\pi(1/10+ih)
       =\frac{\sin(\pi/5)}{\cosh(2\pi h)-\cos(\pi/5)}.
\]
The same written inequalities as in the
[negative four/four face](research_mixed_first_four_four_negative_height_face.md),
Section 3, give
\[
 C_a(h)>245/144>3/2,\qquad
 \Re\cot\pi(t+i\eta)\le3/2
                 \quad(1/5\le t<1,\ \eta\in\mathbb R).
\tag{15}
\]
For completeness, \(2\pi|h|<1/2\) and
\(\cosh u\le1+u^2/[2(1-u^2/12)]\) give
\(\cosh(2\pi h)<53/47<8/7\). The pentagon bounds
\(\cos(\pi/5)>4/5,\ \sin(\pi/5)>7/12\) prove the first
inequality. For the second, a nonnegative real cotangent is no
larger than its height-zero value, and
\(\cot^2(\pi/5)=1+2/\sqrt5<2<9/4\); for \(t\ge1/2\) its
real part is nonpositive.

The identity \(g''(w)=\pi\cot\pi w-\pi i\) gives, for each
fixed cap or ordinary point in (7), (10),
\[
\begin{split}
 \partial_h^2\Re\Psi(e,a)&=
       \pi\{C_a(h)-\Re\cot\pi(e+a)\}>0,\\
 \partial_h^2\Re Q(s;a,b)&=
       \pi\{C_a(h)-\Re\cot\pi(s+a)\}>0.
\end{split}
\tag{16}
\]
Every shifted real part here is at least .25 and less than one.
All chirps are affine in \(h\), and private penalties are fixed.
The true cap-end rate is constant.

For \(1/2\le t<1-x\), exact differentiation of (8) gives
\[
 \partial_h^2E(t;a,b)=
       \pi\{C_a(h)-\Re\cot\pi(a+t)\}>0.
\tag{17}
\]
Only the first numerator is differentiated, so a second-leg wall
does not change this identity. At \(t=1-x\), continuity of the
integrated logarithm gives the pointwise limit of convex functions,
including \(h=0\). Both wall profiles in (10) are therefore convex.
The endpoint carrier (9) is affine. Finally
\(\partial_h^2(-\Re g(a))=\pi C_a(h)>0\), and the other Fourier
branch is constant. Maxima, suprema over fixed sets, and sums preserve
convexity. Consequently \(\mathcal E(h,b)\) is convex on \([c,0]\)
for each fixed \(b\). This is convexity of the proved signed-block
upper envelope, not of the finite modulus and not of the omitted
absolute wrapped-row envelope.

## 4. Individual endpoint calibrations

We first verify the actual-height endpoint before using the
complete-pair bound. At \(h=c\), the bare cap envelope \(A\)
becomes the cap envelope \(\mathcal A\) of that source after adding
the first halfweight: \(\mathcal A=A-\Re g(a)/2\). Likewise the
allocated row rate is \(\mathcal R=E-\Re g(a)/2\).

The [joint low/half-row theorem](research_mixed_early_joint_low_tail.md),
equation (23), pays every cap alternative times both real cuts by
\(\Gamma(z)-1/2000\). If \(h_s\le0\), Sections 2--3 of the
[complete joint central source](research_mixed_early_joint_central_source.md)
pay each cap profile times every main point and every downward
zero-mode join, with reserve at least \(\gamma_*\).
If \(h_s\ge0\), Sections 3--6 of the
[positive-private-height source](research_mixed_early_four_three_positive_private_central.md)
pay the corresponding main and upward joins, with reserve
\(\gamma_{43}\). Its cap cuts, lower alias, upper alias and true
ends are all estimated individually. These are inequalities for
the raw profiles, not consequences of the final signed central
sum.

Those source proofs use an upper alias at height four. To pay
the common height \(1/5\) in (10), use directly the argument
identity in Section 7 of the
[complete selected early source](research_mixed_selected_four_three_early_complete_source.md).
For \(v\in[.15,.5]\), \(x=.1\le z\), all finite private heights
and either outer height sign, its three real-order cases give
\[
 -7\pi/5<\Im Q_s<24\pi/25.
\tag{18}
\]
This proof uses only the original radial argument bounds and
\(x\le z\); it has no positive-first-height hypothesis.
Comparing with the same main point at \(h_s\in[-.065,.068]\),
the lower and upper aliases at \(\pm.2\) have positive reserves
\(\{.4-(24/25)(.268)\}\pi\) and
\(\{.4-(7/5)(.265)\}\pi\), respectively. Both weighted vertical
halves decrease away from the real cut, since the interval in
(18) lies strictly inside \((-2\pi,2\pi)\). These comparisons
remain pointwise after multiplying by any cap profile. Thus
every member of \(\mathscr C_0\) is paid at \(h=c\), without
deducing a smaller-height rate from a height-four estimate.

Section 5 of the [unwrapped high-row proof](research_mixed_unwrapped_stationary_high_row_transport.md)
gives the rate inequality for every cap profile and every
\(t\in[1/2,1-z]\), with reserve \(2\gamma_*\). The
[last-row calibration](research_mixed_first_four_three_true_last_row_calibration.md),
Theorem 1, gives the same individual-profile statement for \(E(1)\)
with reserve \(\gamma_*\); reflection (14) includes \(E(1-x)\).
These are exactly the two signed-wall comparisons (10)--(12)
of the complete-pair theorem. Thus neither wall is inferred from
a possibly vanishing finite coefficient.

At this negative height \(\Re g(a)=G_{-c}(x)\le0\), by the
original radial primitive, so the factorial Fourier alternative
dominates the forcing alternative. We have proved for the entire
envelope
\[
                     \mathcal E(c,b)\le\Gamma(z)-\gamma_{43}.
\tag{19}
\]

At \(h=0\), Proposition 2 of the
[complete four/three real face](research_mixed_selected_four_three_zero_height_face.md)
pays every cap alternative times every member of \(\mathscr C_0\)
and every continuous physical-tail rate, with both Fourier upper
alternatives, by \(\Lambda(z)-1/1000\). It therefore includes
both wall rates, the unwrapped supremum and the last carrier in
(10). Its true-end constant agrees with (7). At zero height the
selected and unselected monomials have the same modulus. Hence
\[
                     \mathcal E(0,b)\le\Lambda(z)-1/1000.
\tag{20}
\]

## 5. The connection and its scope

Let \(\theta=(h-c)/(-c)\). Convexity and (19)--(20) give
\[
\begin{split}
 \mathcal E(h,b)
 &\le(1-\theta)\{\Gamma(z)-\gamma_{43}\}
                +\theta\{\Lambda(z)-1/1000\}\\
 &=\Lambda(z)-(1-\theta)\kappa(z-b_0)^2
             -(1-\theta)\gamma_{43}-\theta/1000\\
 &\le\Lambda(z)-\gamma_{43}.
\end{split}
\tag{21}
\]
The original outgoing quadratic remains explicit until the last
inequality. Combining (11) and (21) proves (6).

All cap inputs are uniform on the whole real ordinary-color
interval. The exact source has degree less than \(N\) in that
color. The interval polynomial continuation in the
[horizontal complex-extension theorem](research_mixed_horizontal_complex_extension.md)
therefore supplies fixed disks at any prescribed extra rate cost,
uniformly in \(h,z\). Cauchy's formula on smaller disks gives fixed
jets. The continuation is from the whole real interval, not from
one complete-color value or a cancellation remainder at one point.

The literal differential on the vertical segment is \(da=i\,dh\).
Its fixed length and original multiplicative measure change only
the prefactor. Thus its oriented integral has the same bound, with
the unchanged external scalar in any original boundary chart.
No selected factor has been inserted into this negative-height
claim. A separate estimate is required for the selected positive
connection, the real first-coordinate interval, the right connector,
other coordinate departures and any whole-period assembly. No
whole-word nonzero coefficient or knot conclusion is asserted here.

## Direct source versions

| Source | SHA-256 |
|---|---|
| research_mixed_early_four_three_complete_pair.md | 271c54a8c5bb9a9fd292dcc66bc760f2cd637f8a685d14fa6722f1eab4d70575 |
| research_mixed_selected_four_three_finite_reduction.md | 732d6cbf79894cb1e230e4eefa27762e369d84127d67e9e7c0d66c77901bbd42 |
| research_mixed_negative_height_wrapped_contour.md | 0f024a3f54087ab3b4fee6f6c992a2e9292644590fc78b21072d6104a0f5c2e6 |
| research_mixed_first_four_three_true_last_row_calibration.md | a1571017529473e88dad8c0f5ec4f3592984a19040962e8279ca9dadb92257de |
| research_mixed_unwrapped_stationary_high_row_transport.md | 24210764f62ef04250a63dbcb5b5e82d4bdf59ede7eacb88889e5318dfc4d4aa |
| research_mixed_early_joint_low_tail.md | 72ee3edebe390f213751e7774913d7d6552d6eff3bdea61b13f4d23159ad6606 |
| research_mixed_early_joint_central_source.md | f19a7b5c42a4f372e9671c95dec5670f501065802fa96279b542efaa5005aec3 |
| research_mixed_early_four_three_positive_private_central.md | b8ffb45bbb9eae0d144b0c2e219207509aa7a119543560b058dfca1734e7c289 |
| research_mixed_selected_four_three_zero_height_face.md | f2c781f91df31cbb892f34d76c5ca5c4deac6e6cd4eda0ac7514bbe3f1ecdd36 |
| research_mixed_selected_four_three_early_complete_source.md | c0f4532b7f8d04c3bc4d84f16435029625c469adf1282914f80bf019bd22ebd6 |
| research_mixed_cap_early_fixed_height_full_source.md | d930407eaa5a0bb7c735ee9521c6d352f637124c57c5593cbb1813f069f7d423 |
| research_mixed_first_attached_low_row_transport.md | 8ef728d3808e1480d85a81c1ed8f7eebda99392d0b11f1262e4a47b5a2b196d3 |
| research_mixed_right_tail_reflection.md | e3928f2d9549159f6955c654b202dc87198137f4cfdb80f85151af567a976ce1 |
| research_mixed_conditional_contour_allowance.md | 12b80f46ea2778c3617fc39099a321592605f07677b9a424ba3153851d037f70 |
| exact_factorial_interpolation_and_complex_contours.md | 1f34f65437dfe0bfb4062a7a74840beae1676353cf13bb8a86f8849a8a36bc72 |
| research_mixed_fourier_weight_continuation.md | 0bae41d83f414eb91fd137de1242120a11408147d56ec752e466ca5ed7e7f48e |
| research_mixed_horizontal_complex_extension.md | c7837a9dfb072f2e276f5ccdb99c7421e154a4ca073a078540d8064dbb3747d4 |
| research_mixed_first_four_four_negative_height_face.md | f50598305505a5dde4537fc15d6ed114b8e3a01eb87d69cff5ac36e0829b40a3 |

The complete written proof and directly used source implications were
read. No mathematical numerical evaluation, saved-value arithmetic,
import, test, compilation or frozen-source edit was performed.
