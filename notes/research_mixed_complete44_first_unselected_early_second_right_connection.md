# The unselected first right connection over the early second interval

Private written deduction, 11 November 2026. This note completes the
unselected first connection from \(9/20+ic_1\) to \(1/2+ic_1\)
and then to \(1/2\), with the second coordinate in
\([1/10,11/50]+ic_2\). The first cap and both conditional sums
remain complete. The horizontal comparison acts on the combined
cap and first conditional rate; the vertical comparison uses convex
functions of height. Neither step assumes monotonicity or convexity
of the modulus of a finite signed sum.

## 1. Source, parameters and statement

Fix an actual positive three/four word of length \(m\ge4\) beginning
with \(444\), with the coupled reference and original normalizations
of [the early second-interval theorem](research_mixed_complete44_second_early_central_four.md).
Write its first three retained references as \(r_j=a_j+ic_j\), and put
\[
 E=[1/10,11/50],\qquad P=[11/50,9/20],\qquad
 y=q+ic_2,\ q\in E,\qquad z=u+ic_3,\ u\in P .
 \tag{1}
\]
The containing bounds used below are
\[
 -.078<c_1<-.020,\qquad
 -.108<c_2,c_3,h_s,h_t<-.001,\qquad
 -.051<h_e<-.019 .
 \tag{2}
\]
These are bounds on the same actual reference. In particular the
third vertex, also when \(m=4\), has its original attached following
leg. No independent parameter rectangle is substituted for that
reference in a calibrated action.

With \(r_N=e^{-2\pi i/N}\), set
\[
 P_j=(r_N;r_N)_j,\quad p_j(V)=(r_NV;r_N)_j,\quad
 X=e^{-2\pi ia},\quad Y=e^{-2\pi iy},\quad Z=e^{-2\pi iz},
\]
\[
 U_{1,N}(w,X)=\sum_{i<N}\frac{H_N(w,r_N^{-i})p_i(X)}{P_i^2},
 \qquad
 C_{1,N}(X,Y)=\sum_{j<N}X^{-j}\frac{p_j(X)p_j(Y)}{P_j^3}.
 \tag{3}
\]
The polynomial \(d_N\), of degree less than \(N\), is the original
interpolation of \(d_N(r_N^j)=P_j^{-1}\). Its forcing is retained.
The density considered here is
\[
 \mathscr K_N=
 U_{1,N}(w,X)d_N(X)C_{1,N}(X,Y)d_N(Y)C_{1,N}(Y,Z).
 \tag{4}
\]
There is no selected first or second monomial in (4).
The outgoing factor is \(|d_N(Z)|^{1/2}\), including at its zeros.

Use \(g(v)=J(v)+i\pi(v-v^2)/2\), \(J'(v)=\Log(2\sin\pi v)\),
with the original branches and absolute constants. The bare phases are
\[
 \Psi(e,a)=S(e)+g(e+a)-g(a)-g(e)-\frac{i\pi}{2}(e-e^2),
\]
\[
 Q(s;a,y)=g(s+a)+g(s+y)-3g(s)-g(a)-g(y)+2\pi ias .
 \tag{5}
\]
Here \(S\) is the original complete endpoint-coefficient action.
Let \(\Lambda_{123}(z)\) be the unchanged affine action
\[
 \Re\{L_1(r_1)+\phi_2(r_1,r_2)+\phi_3(r_2,r_3)
                +\partial_2\phi_3(r_2,r_3)(z-r_3)\},
 \tag{6}
\]
where \(L_1\) is the stationary action of \(\Psi-g(a)/2\), and
\(\phi_2,\phi_3\) are those of \(Q-g(a)/2-g(y)/2\).

Orient the paths successively:
\[
 \Gamma_-=[9/20,1/2]+ic_1,\qquad
 \Gamma_{\mathrm v}=\{1/2+ih:c_1\le h\le0\}.
 \tag{7}
\]

**Theorem.** Uniformly on (1), for both level parities and a sufficiently
small fixed ordinary-color disk about \(-2\),
\[
 |\mathscr K_N|\,|d_N(Z)|^{1/2}
 \le C N^B\exp N\{\Lambda_{123}(z)-10^{-12}\},
 \qquad a\in\Gamma_-\cup\Gamma_{\mathrm v}.
 \tag{8}
\]
The original oriented integrals with density \(N\,da\) have the same
rate and a polynomial prefactor. Fixed ordinary-color derivatives
obey a smaller positive gap on a smaller disk.

## 2. The common profiles and the calibrated starting face

Retain the five regular cap families
\[
\begin{array}{ll}
 \Re\Psi(v+ih_e,a),& .27\le v\le.49,\\
 \Re\Psi(.27,a),\quad \Re\Psi(.49,a),&\\
 \Re\Psi(v-.055i,a)-.11\pi,& .27\le v\le.49,\\
 \Re\Psi(v+.04i,a)-.08\pi,& .27\le v\le.49,
\end{array}
 \tag{9}
\]
and the common constant true-end ceiling
\[
 E_*=\frac35+\frac{2\pi}{100}+\frac{\log4}{100}<\frac{69}{100}.
 \tag{10}
\]
The full cap envelope on the horizontal path is supplied by
[cap support through one half](research_mixed_cap_upper_target_completion.md).
The common-envelope argument in Section 2 of
[the selected right connection](research_mixed_complete44_first_selected_early_second_right_connection.md)
also supplies (9)--(10) at \(a=1/2+ih\), \(c_1\le h\le0\).
It retains the cap's joins, aliases, compact physical tails and
true ends before taking the maximum. The constant (10) is larger
than their actual nonpositive-height endpoint ceiling.

The first ordinary controlling profiles are its fixed main line
\(\Re Q(v+ih_s;a,y)\), \(1/8\le v<1/2\), its left real cut,
and its continuous physical rates
\[
 E_1(t;a,y)=I_a(t)+I_y(t)-3J(t)-2\pi t\Im a,\qquad
 I_b(t)=\int_0^t\log|1-e^{-2\pi i(b+v)}|\,dv .
 \tag{11}
\]
For the third factor retain its actual main line, both real cuts,
and the last carrier:
\[
 D_3(y,z)=\max\left\{
 \sup_{1/8\le t\le1/2}\Re Q(t+ih_t;y,z),
 \Re Q(1/8;y,z),\Re Q(1/2;y,z),-2\pi c_2\right\}.
 \tag{12}
\]
The complete third-source reduction, including all its middle
corrections and all physical rows, is Section 5 of the early
second-interval theorem. It is unchanged by any motion of \(a\).

At \(a=9/20+ic_1\), Sections 2--5 of that theorem bound every
regular cap/main or cap/cut comparison, and every first high
physical rate, with each third profile in (12). With the rates
of the two internal and the outgoing Fourier weights attached,
the common raw bound is
\[
                       \Lambda_{123}(z)-\eta,\qquad \eta=10^{-10}.
 \tag{13}
\]
This is the profile comparison before finite summation in that
proof. It is not inferred by separating terms in a bounded signed sum.
Its cap input is the allocated plane \(B_L\).

Replacing the cap by the larger constant (10) leaves an extra
reserve. The cap-support proof gives \(B_T>149/200\), and its
allocation identity gives
\[
 B_L(x)-\{E_*-\tfrac12\Re g(x+ic_1)\}
 >\frac{149}{200}-\frac{69}{100}=\frac{11}{200}.
 \tag{14}
\]
Thus every constant-cap comparison at this face has (13) with
the additional loss \(11/200\).

Choose a fixed small \(\varepsilon>0\), and write \(r_0=1/2-\varepsilon\).
Uniform continuity of the integrated physical rates permits the
additional collar \(r_0\le t\le1/2\) in (13), with \(\eta/2\)
in place of \(\eta\). Decrease \(\varepsilon\) also to fit the
collar in the selected right-connection theorem at \(a=1/2\).
All these choices are made before \(N\). Numerator zeros cause
no loss of continuity in their integrated rates.

## 3. Horizontal transport of the combined profiles

Put \(r=e^{2\pi c_1}\), and let \(9/20\le x\le1/2\).
The actual first-height bound gives \(r>20/33>3/5\).
For a fixed cap point \(e\) in (9), and a main point \(s=v+ih_s\),
put
\[
 D=|1-r e^{-2\pi ix}|,\quad
 N_e=|1-r e^{2\pi\Im e}e^{-2\pi i(x+\Re e)}|,\quad
 T_s=e^{-2\pi h_s},\quad
 N_s=|T_s-r e^{-2\pi i(x+v)}|.
 \tag{15}
\]
The numerator \(N_s\) includes the incoming chirp in (5).
Dropping that chirp would give a different derivative.

The bounds already used in
[the unselected right-half proof](research_mixed_initial44_right_half_interval.md)
give
\[
 D^2>1+r^2+\frac{19}{10}r,\qquad
 e^{2\pi\Im e}<\frac43,\qquad T_s<2.
 \tag{16}
\]
For the last assertion, \(2\pi|h_s|<.216\pi<17/25<\log2\);
the elementary witness \(\log2>56/81\) suffices.
Also \(.72\le x+\Re e\le.99\), so
\(\cos(2\pi(x+\Re e))>-1/5\).
At its smallest endpoint this follows from
\(\sin(3\pi/50)<1/5\). Consequently
\[
 N_e^2\le1+\frac{16}{9}r^2+\frac8{15}r
       <\frac9{10}\left(1+r^2+\frac{19}{10}r\right)
       <\frac9{10}D^2 .
 \tag{17}
\]
To verify the middle inequality, subtract its left side from the
middle expression. The result is the concave quadratic
\[
 -\frac1{10}+\frac{353}{300}r-\frac{79}{90}r^2.
 \tag{18}
\]
At \(r=3/5\) it is \(29/100\), and at \(r=1\) it is
\(179/900\), both positive. Concavity proves the inequality
throughout \([3/5,1]\).

It follows that \(N_e<(19/20)D\). Moreover \(N_s<2+r\), and
\[
 D^2-\frac{19}{20}(2+r)
 >r^2+\frac{19}{20}r-\frac9{10}\ge\frac3{100}.
 \tag{19}
\]
The polynomial increases on \([3/5,1]\), and its left value is
\(3/100\). Exact differentiation, retaining the chirp, therefore gives
\[
 \partial_x\{\Re\Psi(e,a)-p_e+\Re Q(s;a,y)-\Re g(a)\}
             =\log\frac{N_eN_s}{D^3}<0 .
 \tag{20}
\]
Here \(p_e\) denotes the fixed cap penalty; the next kernel and
its allocations are constant during this motion.

For a constant cap ceiling, the derivative instead is
\[
 \log\frac{N_s}{D^2}
 \le\log\frac{2+r}{1+r^2+19r/10}
 \le\log\frac{26}{25}<\frac1{25}.
 \tag{21}
\]
The rational quotient decreases for \(r\ge3/5\): the numerator
of its derivative is \(-r^2-4r-14/5<0\).
Its value at \(3/5\) is \(26/25\).
Over an interval of length \(1/20\), the increase is less than
\(1/500\). The extra reserve \(11/200\) in (14) pays this
increase. Thus constant-cap main profiles retain (13).

For a real physical index \(t\ge1/8\), the chirp does not change
under motion of \(x\), and its derivative numerator is
\[
                       N_t=|1-r e^{-2\pi i(x+t)}|\le D .
 \tag{22}
\]
Indeed \(1-2x\le t\le1\), and
\(\cos(2\pi(x+t))\ge\cos(2\pi x)\).
This applies through the moving numerator walls by continuity
of the integrated rates. Equations (17), (22) show that the
regular-cap derivative is negative; for a constant cap it is
\(\log(N_t/D^2)\le-\log D<0\).
Every real cut, collar and high profile therefore transports
with its full reserve from the initial face.

The complete first Fourier rate used in these formulas is
\(-\Re g(a)\). The lower-disk primitive is nonpositive for
\(0<x\le1/2\), so this bounds both alternatives of \(d_N\).
At \(x=1/2\) the rate is zero, and no relative approximation
or division by \(d_N\) is used.

We have proved the raw horizontal bound
\(\Lambda_{123}-\eta/2\) for every controlling first main,
cut, collar and high profile with every cap and third profile.
The central corrections are included in Section 5 below.

## 4. The negative-height connection at one half

Let \(a_h=1/2+ih\), \(c_1\le h\le0\), with the private
heights fixed. The horizontal argument calibrates all the
controlling profiles at \(h=c_1\).
At \(h=0\), Sections 3--4 of the selected right-connection
theorem calibrate the same cap profiles, main points, real
cuts and collar, with every third profile in (12), at gap
\[
 \delta_R=\frac1{2500000}(9/20-a_1)^2
                         >\frac1{250000000}>\eta/2 .
 \tag{23}
\]
At zero height the selected monomial has modulus one, and both
first Fourier upper rates are zero.

For each fixed cap and main point, respectively,
\[
 \frac{d^2}{dh^2}\Re\Psi(e,a_h)
      =-\pi\Re\cot\pi(e+a_h)>0,\qquad
 \frac{d^2}{dh^2}\Re Q(s;a_h,y)
      =-\pi\Re\cot\pi(s+a_h)>0 .
 \tag{24}
\]
Their shifted real parts lie strictly between \(1/2\) and one.
The penalties are constant and the chirp is affine in \(h\).
The cap true-end ceiling is constant. The same convexity holds
for (11) when \(t\le1/2\); the half-index limit is continuous
and remains convex even at the real wall.
Thus the endpoint bounds control each cap/main, cap/cut and
cap/collar profile throughout this height interval.

For higher physical rows apply
[the all-angle own-four theorem](research_mixed_complete44_two_early_angles_high_rows.md):
\[
 E_1(t;a_h,y)\le
       \max\{E_1(1/2;a_h,y),-2\pi h\},\qquad 1/2\le t\le1 .
 \tag{25}
\]
The theorem is printed for first angle less than \(1/2\).
Its integrated inequality extends to the endpoint by continuity.
Its zero-safe finite-product proof is uniform there as well:
the possible moving zeros remain simple, with the same uniform
integrable logarithmic bound. It therefore retains every finite
row through \(N-1\) at both parities.

The second carrier in (25) is affine in \(h\). At \(h=c_1\)
its joint cap comparison is already paid by the horizontal
last-rate estimate. At \(h=0\) it is zero, and is no larger
than the half rate. The latter follows from the
[zero-drift high-row inequality](research_mixed_all_angle_high_row_sign_class.md),
including its continuous endpoint \(t=1\).
Hence each cap profile plus this carrier is convex with both
endpoints paid. This controls every high physical row in (25).
The first Fourier upper rate is identically zero on this
half-face interval, since \(\Re g(1/2+ih)=0\).
All controlling profiles retain gap \(\eta/2\).

## 5. Low rows, the exact middle contour and all its corrections

Use fixed cuts tending to \(1/8,r_0\):
\[
 L_N=\lfloor N/8\rfloor+1,\qquad K_N=\lceil Nr_0\rceil .
 \tag{26}
\]
For either path in (7), the incoming radius satisfies \(0<r\le1\)
and \(9/20\le\Re a\le1/2\).
For \(0<t\le1/8\), the incoming numerator divided by \(r\)
exceeds \(\sqrt2>7/5\), because
\(\cos(2\pi(\Re a+t))<0\). The outgoing numerator
\(|1-e^{2\pi c_2-2\pi i(q+t)}|\) exceeds \(1/2\):
its radial minimum on \(q+t\in[.1,.345]\) is at least
\(\sin(\pi/5)>1/2\) before \(1/4\), and at least one afterwards.
Finally \(2\sin(\pi t)<4/5\). The exact consecutive-row ratio
is therefore greater than
\[
               \frac{(7/5)(1/2)}{(4/5)^3}
                          =\frac{175}{128}>1 .
 \tag{27}
\]
All numerator factors in this low range are nonzero. The low
finite block is bounded by a fixed multiple of its last row,
whose rate is the paid left cut. The possible \(O(1/N)\)
displacement is absorbed in the source allowance.

For the middle block keep the marked interpolant
\[
 e^{2\pi iNas}\Pi_N(a+s)\Pi_N(y+s)
                      E_N(a)E_N(y)E_N(s)^3,
 \quad
 \Pi_N(v)=\widehat P_N(Nv),\quad E_N(v)=\Pi_N(v)^{-1}.
 \tag{28}
\]
The negative-root marking is exactly that in
[Fourier-weight continuation](research_mixed_fourier_weight_continuation.md).
The half-grid rectangle has lower height \(-1/5\), upper height
four, and real cuts tending to \(1/8,r_0\).
Every factorial argument stays in a fixed compact substrip
of \(0<\Re v<1\); in particular
\(\Re(a+s)\le1-\varepsilon+o(1)\).
The [factorial interpolation theorem](exact_factorial_interpolation_and_complex_contours.md)
therefore applies at all these fixed heights.
The exact residue coefficient is \(N/(2i)\); moving its zero
mode to \(h_s\) retains its positive density \(N\), both unweighted
joins, both horizontal aliases and all four weighted vertical halves.

Here is a uniform bound for those corrections. For
\(s=v+i\sigma\), write \(I=\Im Q_s\), with the original
logarithmic lifts. The real part \(v+\Re a\) is above one half.
The elementary regular-strip argument bounds used in the
unselected right-half proof give
\[
                         -\frac32\pi<I<\frac{31}{20}\pi .
 \tag{29}
\]
For clarity, if \(q+v\ge1/2\), the lower and upper bounds
divided by \(\pi\) are \(-1+2v-2q\ge-119/100\) and
\(2\Re a\le1\). If \(q+v<1/2\), they are
\(-2+4v\ge-3/2\) and
\(1-2v-2q+2\Re a\le31/20\).
These inequalities are independent of all imaginary coordinates.
They retain the incoming carrier \(2\pi\Re a\).

The lower horizontal alias consequently loses at least
\[
             \frac{2\pi}{5}-\frac{31\pi}{20}\frac15
                            =\frac{9\pi}{100}
 \tag{30}
\]
against the same main point. The upper alias loses at least
\[
               8\pi-\frac{3\pi}{2}(4+.108)
                              =\frac{919\pi}{500}.
 \tag{31}
\]
Both sampling penalties have been kept.
On a lower vertical half, the derivative of
\(\Re Q+2\pi\sigma\) is greater than \(9\pi/20\);
on an upper half, that of \(\Re Q-2\pi\sigma\)
is less than \(-\pi/2\). Thus the weighted halves reduce
to their real-cut endpoints.

On an unweighted join, \(h_s\le\sigma\le0\).
The incoming shifted real cotangent is negative.
If the outgoing shifted real cotangent is positive, it is
at most \(C=\Re\cot\pi s>0\), by the negative-height
cotangent comparison in Section 6 of the selected right-connection
proof. Its hypotheses are unchanged: \(v\ge1/8\),
\(|\sigma|\le.108\), \(q>0\), and \(c_2<0\).
Hence
\[
                3C-\Re\cot\pi(s+a)-\Re\cot\pi(s+y)>0 .
 \tag{32}
\]
The real phase is convex in the private height. Each unweighted
join is bounded by its already paid main and real-cut endpoints.
These arguments also include the new right cut and its half-grid
displacement. The wall at \(a+s=1\) belongs only to the physical
block; it never lies on an interpolation side.

The complete third conditional source remains the one in (12).
Every cap alternative was retained before pairing with it.
Thus the preceding comparisons pay every product of the original
main terms, corrections and physical blocks.

## 6. Finite assembly and scope

The [whole Fourier upper bound](research_mixed_fourier_weight_continuation.md)
supplies exactly \(-\Re g(a)\) on the horizontal path, zero
on the half-face vertical, \(-\Re g(y)\) internally, and
\(-\Re g(z)/2\) at the outgoing allocation.
These are precisely the incidences of (4).
No factor is divided out, and zeros remain permitted.

All raw controlling profiles have gap at least \(\eta/2\).
Choose the finitely many factorial, row and color allowances
within this reserve. Their row counts, densities, fixed contour
lengths and symbols cost polynomial factors. This proves (8).
The cap source supplies the fixed ordinary-color disk after the
allowance is chosen; Cauchy's formula gives fixed derivatives on
a smaller disk. The actual measures are \(da=dx\) horizontally
and \(da=i\,dh\) vertically.

Combined with the preceding first-left estimates, this completes
the unselected deformed path from zero to \(1/2\) for the stated
early second targets. The real first arc \([1/2,1]\) is not
included. The full first remainder there, the full second period,
and stability under arbitrary short attachments remain separate.
No extension to an initial \(443\) or a whole-knot conclusion
is asserted here.

## Direct source versions

| Source | SHA-256 |
|---|---|
| research_mixed_complete44_second_early_central_four.md | e5be8082613eac6887d3aca857703e4ac5b511c430f35ca91fa388c71a924f45 |
| research_mixed_initial44_right_half_interval.md | 309d6869f7438a9ed0a407c43666198ce1a039db7545c404a5e97f4ba2538c9c |
| research_mixed_cap_upper_target_completion.md | 49292f204a86e08c48c5aa8fd29f98103f38a939bb88d523afdd8be741650c22 |
| research_mixed_complete44_first_selected_early_second_right_connection.md | 4a0ec064b1f408351088e386e3cba2c4bdf2ee852f2c3027687394fa0626ea58 |
| research_mixed_complete44_two_early_angles_high_rows.md | b088d7b6e388f65f3a96e9176f810cfd0936cb31f425e47fcd9808c6dcb81c8d |
| research_mixed_all_angle_high_row_sign_class.md | 3a959f0a6bb064767e753e90061a2d9ef323268e79cbdf19c1043a6fe9691144 |
| research_mixed_fourier_weight_continuation.md | 0bae41d83f414eb91fd137de1242120a11408147d56ec752e466ca5ed7e7f48e |
| exact_factorial_interpolation_and_complex_contours.md | 1f34f65437dfe0bfb4062a7a74840beae1676353cf13bb8a86f8849a8a36bc72 |

Author full proof readback and all eight directly used source
implication reads and source-hash checks are complete. A separate
full proof and direct-source review is required before adoption.
No mathematical numerical evaluation, saved-value arithmetic,
import, test or compilation was used.
