# The complete unselected first-four/four negative-height face

Private written proof, 10 November 2026. The first retained coordinate
can move vertically from its actual negative height to zero at real
part one tenth, while the second coordinate keeps its actual height.
The complete original first-four/four source stays strictly below its
original joint affine rate. The proof uses a single convex upper
envelope for every finite current at both ends. In particular, its
ordinary upper alias has height four, as in the negative-height
source theorem. A bound on a cancelling whole sum is not used as
a bound on its individual profiles.

## 1. Actual reference and literal source

Fix an actual positive three/four open word of length at least three
beginning with four and four. Retain its original reference and
markings. Write
\[
 a_*=a_0+ic,\qquad b_*=b_0+id,\qquad
 e_*=u_*+ih_e,\quad s_*=v_*+ih_s.
\]
The actual source bounds used in the
[complete first-four/four theorem](research_mixed_first_four_four_true_last_row_calibration.md)
give
\[
 .246<a_0<.350,\quad -39/500<c<-1/50,\quad
 -.102<d<0,\quad -.108\le h_s<0,\quad
 -.051<h_e<-.019.
\tag{1}
\]
Only the target first height moves:
\[
 a=\frac1{10}+ih,\qquad c\le h\le0,\qquad
 b=z+id,\qquad z\in P=[11/50,9/20].
\tag{2}
\]
The containing inequalities in (1) do not replace the actual coupled
reference by an arbitrary point of a box.

For \(q_N=e^{-2\pi i/N}\), put
\[
 P_j=(q_N;q_N)_j,\quad p_j(X)=(q_NX;q_N)_j,\quad
 X=e^{-2\pi ia},\quad Y=e^{-2\pi ib}.
\]
Keep exactly
\[
\begin{split}
 U_{1,N}(w,X)&=\sum_{i=0}^{N-1}
           \frac{H_N(w,q_N^{-i})p_i(X)}{P_i^2},\\
 C_{1,N}(X,Y)&=\sum_{j=0}^{N-1}R_{j,N}(a,b),\qquad
 R_{j,N}=X^{-j}\frac{p_j(X)p_j(Y)}{P_j^3},\\
 \mathcal K_N^{\,0}(w;a,b)&=U_{1,N}(w,X)C_{1,N}(X,Y)d_N(X).
\end{split}
\tag{3}
\]
Here \(H_N\) is the complete original cap coefficient. The outgoing
allocation is \(|d_N(Y)|^{1/2}\). The whole first weight \(d_N(X)\)
is retained; no selected monomial is present in (3). No scalar,
physical row or terminal marking is changed.

Use the original bare phases
\[
\begin{split}
 \Psi(e,a)&=S(e)+g(e+a)-g(a)-g(e)-\frac{i\pi}{2}(e-e^2),\\
 Q(s;a,b)&=g(s+a)+g(s+b)-3g(s)-g(a)-g(b)+2\pi ias,\\
 \mathcal F(e,s;a,b)&=\Psi(e,a)+Q(s;a,b)-g(a)-\tfrac12g(b),\\
 M&=\Re\mathcal F(e_*,s_*;a_*,b_*),\qquad
 p=\mathcal F_b(e_*,s_*;a_*,b_*),\\
 \Lambda(z)&=M+\Re p\,(z-b_0),\qquad
 \Gamma(z)=\Lambda(z)-\kappa(z-b_0)^2,\\
 \kappa&=1/2500000,\qquad
 \gamma_{44}=\kappa(a_0-11/50)^2>0.
\end{split}
\tag{4}
\]
All branches and constants in \(S,g\) are unchanged. The allocated
phases of the first-four/four theorem are precisely
\(\Xi=\Psi-g(a)/2\) and \(F=Q-g(a)/2-g(b)/2\).
Their sum is \(\mathcal F\), so (4) is the same original plane,
including its outgoing marginal. In particular
\[
 \gamma_{44}>\kappa(13/500)^2,\qquad
                         \gamma_{44}<1/1000.
\tag{5}
\]

**Theorem 1.** For every \(\tau>0\), the literal source satisfies
\[
 |\mathcal K_N^{\,0}(w;a,b)|\,|d_N(Y)|^{1/2}
 \le C_\tau N^{A_\tau}
             \exp N\{\Lambda(z)-\gamma_{44}+\tau\}
\tag{6}
\]
uniformly on (2), at both level parities, and for every real ordinary
color \(w\in[-2,2]\). The same rate holds on a sufficiently small fixed
ordinary-color disk about \(-2\), with any prescribed total allowance
\(\tau\); fixed derivatives hold on smaller disks with polynomial cost.
The bound also pays the literal oriented vertical integral in \(a\),
with the same outgoing modulus allocation and original external scalar.

## 2. A common complete envelope

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
                         A_*(h)=\frac35+\frac{\log4}{100}.
\tag{7}
\]
The [independent-height complete cap source](research_mixed_cap_early_fixed_height_full_source.md)
applies on the entire rectangle containing (2). Its own-four
upper-row allowance is zero. Its general true-end ceiling is
\(3/5+2\pi h_++\log4/100\), hence is exactly (7) throughout this
negative-height face. All cap zero-mode joins, aliases, physical
tails and both true ends are included.

Define \(\mathscr C_4\) as the following full collection of ordinary
private points and penalties, with \(v\in[1/8,1/2]\):

| Piece | Point \(s\) | Penalty \(\omega\) |
|---|---|---|
| Main zero mode | \(v+ih_s\) | \(0\) |
| Both zero-mode joins | \(\ell+iy,\ \ell\in\{1/8,1/2\},\ h_s\le y\le0\) | \(0\) |
| Lower horizontal alias | \(v-i/5\) | \(2\pi/5\) |
| Upper horizontal alias | \(v+4i\) | \(8\pi\) |
| Four vertical alias halves | \(\ell+iy,\ \ell\in\{1/8,1/2\},\ y\in[-1/5,0]\cup[0,4]\) | \(2\pi|y|\) |

The real cuts occur at \(y=0\). In particular the upper height is
four throughout, rather than the height two used by the positive
join envelope.

Let \(J(t)=\Re g(t)\) on the real interval and retain the integrated
physical-row rate
\[
\begin{split}
 E(t;a,b)={}&\int_0^t\log|1-e^{-2\pi i(a+v)}|\,dv
       +\int_0^t\log|1-e^{-2\pi i(b+v)}|\,dv\\
       &-3J(t)-2\pi ht .
\end{split}
\tag{8}
\]
It is continuous through every integrated numerator zero. The full
period and the incoming chirp give
\[
                              E(1;a,b)=-2\pi h
\tag{9}
\]
because \(h\le0,d<0\). Set
\[
\begin{split}
 B(h,b)&=\max\left\{
     \sup_{(s,\omega)\in\mathscr C_4}\{\Re Q(s;a,b)-\omega\},
     \sup_{1/2\le t\le9/10}E(t;a,b),-2\pi h\right\},\\
 W_0(h)&=\max\{-\Re g(a),0\},\qquad
 q(b)=\tfrac12\max\{-\Re g(b),0\},\\
 \mathcal E(h,b)&=A(h)+B(h,b)+W_0(h)+q(b).
\end{split}
\tag{10}
\]
Thus both upper alternatives of the full unselected Fourier
polynomial are retained. At the present negative heights,
the radial primitive gives \(\Re g(a),\Re g(b)\le0\), so its
factorial branch dominates. Keeping the maxima in (10) makes
explicit that no forcing branch was discarded by assumption.

For every \(\tau>0\), the exact source satisfies
\[
 |\mathcal K_N^{\,0}(w;a,b)|\,|d_N(Y)|^{1/2}
 \le C_\tau N^{A_\tau}e^{N\{\mathcal E(h,b)+\tau\}}.
\tag{11}
\]
Here is the complete finite-source justification. Split its ordinary
rows into
\[
 0\le j\le\lfloor N/8\rfloor,\qquad
 \lfloor N/8\rfloor+1\le j\le\lceil N/2\rceil-1,\qquad
 \lceil N/2\rceil\le j<N.
\tag{12}
\]
The [exact low-row ratio](research_mixed_first_attached_low_row_transport.md)
exceeds \(e^{1/200}\) on the independent outer-height box containing
(2), through index \(N/5\). The first block is therefore bounded by
201 times its last row; its rate tends uniformly to the real-cut
rate \(\Re Q(1/8;a,b)\) already in (10).

For the central block use the original marked factorial interpolant
and half-grid cuts tending to \(1/8,1/2\), with lower height \(-1/5\)
and upper height \(4\). The real arguments remain in compact
subintervals of the original regular strip:
\[
 \Re(s+a)\in[.225,.6],\qquad
 \Re(s+b)\in[.345,.95],\qquad
 \Re a=.1,\quad\Re b\in P.
\]
The [exact factorial theorem](exact_factorial_interpolation_and_complex_contours.md)
allows every fixed compact imaginary-height interval. Its original
cotangent residue identity thus applies without crossing a factorial
pole. The constant modes give density \(+N\); shifting only that
zero mode to \(h_s\) retains both zero-mode joins. The two horizontal
aliases and all four vertical halves have exactly the penalties
in \(\mathscr C_4\). This is the exact construction in Section 6 of
the [joint central source](research_mixed_early_joint_central_source.md),
without importing its fixed-height estimate into interior heights.
Every resulting rate is retained in (10).

For the high block use the original zero-safe product bound before
any summation. Every rate with \(1/2\le t\le9/10\) is present in
(10). For \(9/10\le t\le1\), put \(v=1-t\le1/10\).
The integral proof of the
[reflection lemma](research_mixed_right_tail_reflection.md), Lemma 1,
requires only \(v\le x,z\le1/2\), where here \(x=1/10\). It gives
\[
 E(1-v)-E(1)\le J(v)-(-2\pi h)v\le0.
\tag{13}
\]
The exact reflected drift is retained. This compares continuous
integrated rates, not ratios to a possibly zero finite half or last
row. All zeros, both parity stops and the literal row \(N-1\) are
therefore included. Uniform rounding errors and finite lengths
consume a polynomial and one arbitrarily small tolerance.

The complete cap source and the whole
[Fourier-weight theorem](research_mixed_fourier_weight_continuation.md)
now give (11). The nonpositive radial primitive on \(0\le t\le1/2\)
used after (10) is the same one in the reflection proof. Hence the
original negative-height half allocations agree exactly with (10).

## 3. Convexity on the full actual negative interval

Write
\[
 C_a(h)=\Re\cot\pi(1/10+ih)
       =\frac{\sin(\pi/5)}{\cosh(2\pi h)-\cos(\pi/5)}.
\]
For \(|h|\le39/500\), we have \(2\pi|h|<1/2\).
The positive series bound
\[
 \cosh t\le1+\frac{t^2}{2(1-t^2/12)}
\]
therefore gives \(\cosh(2\pi h)<53/47<8/7\).
The pentagon identities give
\(\cos(\pi/5)>4/5\), \(\sin(\pi/5)>7/12\). Consequently
\[
                         C_a(h)>\frac{245}{144}>\frac32.
\tag{14}
\]
The series bound follows by comparing consecutive even-factorial
terms, whose ratios after the quadratic term are at most \(t^2/12\).
The elementary pentagon inequalities follow from
\(11/5<\sqrt5<9/4\); no evaluated constant is used.

For every finite \(\eta\) and \(1/5\le t<1\),
\[
                    \Re\cot\pi(t+i\eta)\le\frac32.
\tag{15}
\]
For \(t\le1/2\) its explicit denominator bounds it by \(\cot\pi t\),
and \(\cot^2(\pi/5)=1+2/\sqrt5<2<9/4\).
For \(t\ge1/2\) its real part is nonpositive.

Every retained cap numerator \(e+a\) and ordinary numerator \(s+a\)
has real part in \([.225,1)\). The identity
\(g''(z)=\pi\cot\pi z-\pi i\) gives, for every fixed private point,
\[
\begin{split}
 \partial_h^2\Re\Psi(e,a)
     &=\pi\{C_a(h)-\Re\cot\pi(e+a)\}>0,\\
 \partial_h^2\Re Q(s;a,b)
     &=\pi\{C_a(h)-\Re\cot\pi(s+a)\}>0.
\end{split}
\tag{16}
\]
This holds even on the entire upper interval through height four.
The chirps are affine in the outer height, and the alias penalties
are fixed. The cap true-end ceiling (7) is constant here.

For \(1/2\le t<9/10\), the first physical numerator has not
crossed its real wall, so exact differentiation of (8) gives
\[
 \partial_h^2E(t;a,b)
       =\pi\{C_a(h)-\Re\cot\pi(a+t)\}>0.
\tag{17}
\]
Here \(3/5\le\Re(a+t)<1\). The second numerator may be wrapped,
but it is independent of \(h\). At \(t=9/10\), continuity of the
integrated logarithm gives the pointwise limit of convex functions,
also at \(h=0\). The carrier (9) is affine. Finally
\[
                    \partial_h^2\{-\Re g(a)\}=\pi C_a(h)>0.
\]
The other Fourier branch is the constant zero. Taking maxima,
suprema and sums proves that the complete same-source envelope
\(\mathcal E(h,b)\) is convex on \([c,0]\). No convexity of
the finite modulus or its logarithm has been assumed.

## 4. Both endpoint calibrations, before finite summation

At \(h=c\), every cap profile in (7) is exactly the one in the
complete first-four/four source, before allocating its first
halfweight. The low/half comparison in the
[joint low-row theorem](research_mixed_early_joint_low_tail.md),
equation (23), pays each cap alternative times both real cuts
with deficit \(1/2000\).

For every central main point and downward zero-mode join, Sections
2--3 of the joint central source give the profile bound
\(\Gamma(z)-2\gamma_{44}\). Its Sections 4--5 use exactly the
upper height four of \(\mathscr C_4\). In particular
\[
 \Im Q_s>-11\pi/5\quad\hbox{at every height},\qquad
 \Im Q_s>-77\pi/40\quad(y\ge0).
\]
The complete upper horizontal comparison has the original cost
\[
 (11/5)(27/250)\pi+4(77/40)\pi-8\pi=-39\pi/625<0.
\tag{18}
\]
Its lower horizontal comparison is also strictly below the same
main point, and each weighted vertical half decreases away from
its real cut. These comparisons are pointwise in every cap private
coordinate; the separate true-end comparison was retained in its
Section 2. Hence they pay the full raw Cartesian profile inventory,
not only the final central sum.

For the high part, Theorem 1 of the
[own-four high-row theorem](research_mixed_early_own_four_high_rows.md)
states the continuous identity
\[
 \max_{1/2\le t\le1}E(t;a,b)
                       =\max\{E(1/2;a,b),E(1;a,b)\}.
\tag{19}
\]
Its actual hypotheses include \(c>-39/500,d<0\), and it retains
the reflected drift. The cap-times-half profile is the joint
low/half bound just cited. The cap-times-last profile is equation
(36) of the first-four/four calibration:
\[
 \mathcal A(a)+\mathcal R(1;a,b)\le\Gamma(z)-\gamma_{44}.
\]
Here \(\mathcal A=A-\Re g(a)/2\) and
\(\mathcal R=E-\Re g(a)/2-\Re g(b)/2\). Their sum is exactly
the corresponding term in (10). Thus (19) pays every high profile
before summing any finite rows. Both full first Fourier alternatives
are paid because the factorial alternative dominates at this
negative-height target. We have proved
\[
                         \mathcal E(c,b)\le\Gamma(z)-\gamma_{44}.
\tag{20}
\]

At \(h=0\), Proposition 2, equation (34), of the
[complete zero-height face](research_mixed_selected_four_four_zero_height_face.md)
pays every cap alternative times every raw ordinary current and
physical-tail rate, with both Fourier alternatives, by
\(\Lambda(z)-1/1000\). At zero height the selected and unselected
monomials have the same modulus, so its Fourier alternatives are
exactly \(W_0(0)=\max\{-J(1/10),0\}\).

There is one contour difference to check: that proposition uses
upper height two. Its equation (28), however, proves
\(\Im Q_s\ge-77\pi/40\) for every \(y\ge0\), so
\[
 \partial_y\{\Re Q(v+iy;a,b)-2\pi y\}\le-3\pi/40.
\tag{21}
\]
Its upper horizontal rate at height four is therefore no larger
than its paid height-two rate. The extra vertical portions
\(2\le y\le4\) are likewise no larger than their already paid
real-cut rates. All other pieces of \(\mathscr C_4\) coincide with
its inventory. The proposition also includes every physical rate
\(1/2\le t\le1\), including (9)'s value zero. Its true-end ceiling
agrees with (7). Thus, for this common taller envelope,
\[
                         \mathcal E(0,b)\le\Lambda(z)-1/1000.
\tag{22}
\]
This establishes compatibility of raw contours at the endpoints.
No implication from an upper bound at height four to a larger rate
at height two has been used.

## 5. The vertical face, color neighborhoods and remaining scope

Put \(\theta=(h-c)/(-c)\in[0,1]\). Convexity and (20)--(22) give
the slightly stronger explicit rate bound
\[
\begin{split}
 \mathcal E(h,b)
 &\le(1-\theta)\{\Gamma(z)-\gamma_{44}\}
                       +\theta\{\Lambda(z)-1/1000\}\\
 &=\Lambda(z)-(1-\theta)\kappa(z-b_0)^2
                -(1-\theta)\gamma_{44}-\theta/1000\\
 &\le\Lambda(z)-\gamma_{44}.
\end{split}
\tag{23}
\]
Thus the outgoing quadratic is retained until the final inequality.
Combining (11) and (23) proves (6) for every real ordinary color.
All source estimates are uniform on compact parameter sets; their
finite number of tolerances can be chosen inside the one prescribed
\(\tau\).

The literal source has ordinary-color degree less than \(N\).
The interval Chebyshev/Bernstein--Walsh estimate in Section 1 of
the [horizontal complex-extension theorem](research_mixed_horizontal_complex_extension.md)
therefore gives a fixed disk at any prescribed additional rate
cost, uniformly in \(h,z\). Cauchy's formula gives every fixed
ordinary-color derivative on a smaller disk. This continues from
the whole real color interval, not from a single complete-color
value, and never divides by a possibly zero common multiplier.

The vertical segment has fixed length, and its literal differential
in the first additive coordinate is \(da=i\,dh\); the original
multiplicative measure and external scalar are unchanged. Integrating
the uniform bound pays that oriented current as well. The outgoing
half-modulus remains available in exactly the allocation of (3);
the other half belongs to the next adjoining factor.

This proves the unselected negative first-height face only. Combining
it with separate positive and real-segment estimates requires those
estimates in their own source charts. The real segment between the
old collar and \(1/10\), the right outer boundary, later selections
and any remaining whole-period pieces are not inferred from (6).
No whole-word nonzero coefficient, knot invariant or finite-exception
conclusion is asserted.

## Direct source versions

| Source | SHA-256 |
|---|---|
| research_mixed_first_positive_join_convex_envelope.md | b1f18bb5a79ff958654190c960c933ac7839f1da3fc86635f6222a1ea58cb774 |
| research_mixed_first_four_four_true_last_row_calibration.md | 52c149d8500e88c6e4e3fdf1c9e699baf376dfaac8b96d3461dc81f9d1725e0d |
| research_mixed_early_own_four_high_rows.md | 62c3d5070d15c093ae8ab10cb373e9624a497d29743d6cd909bc5d7a33daebb6 |
| research_mixed_early_joint_central_source.md | f19a7b5c42a4f372e9671c95dec5670f501065802fa96279b542efaa5005aec3 |
| research_mixed_early_joint_low_tail.md | 72ee3edebe390f213751e7774913d7d6552d6eff3bdea61b13f4d23159ad6606 |
| research_mixed_selected_four_four_zero_height_face.md | fe99fcefe1618991471f083febcf4c6043418a4387d76be1ae2015542734810f |
| research_mixed_cap_early_fixed_height_full_source.md | d930407eaa5a0bb7c735ee9521c6d352f637124c57c5593cbb1813f069f7d423 |
| research_mixed_first_attached_low_row_transport.md | 8ef728d3808e1480d85a81c1ed8f7eebda99392d0b11f1262e4a47b5a2b196d3 |
| research_mixed_right_tail_reflection.md | e3928f2d9549159f6955c654b202dc87198137f4cfdb80f85151af567a976ce1 |
| exact_factorial_interpolation_and_complex_contours.md | 1f34f65437dfe0bfb4062a7a74840beae1676353cf13bb8a86f8849a8a36bc72 |
| research_mixed_fourier_weight_continuation.md | 0bae41d83f414eb91fd137de1242120a11408147d56ec752e466ca5ed7e7f48e |
| research_mixed_horizontal_complex_extension.md | c7837a9dfb072f2e276f5ccdb99c7421e154a4ca073a078540d8064dbb3747d4 |

The full written proof and directly used source portions were read.
No mathematical numerical evaluation, saved-value arithmetic, import,
test, compilation or frozen-source edit was performed.
