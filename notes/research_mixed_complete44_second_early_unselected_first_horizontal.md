# The full unselected first early horizontal with an early second target

Private written proof, 11 November 2026. For an actual word beginning
with \(444\), the complete cap and both complete conditional kernels
are controlled when both first retained real coordinates lie in
\([1/10,11/50]\), at their original negative heights, and the third
target remains on its original plateau. This extends the completed
old-first-plateau comparison to the unselected early first horizontal.
It retains every finite row and contour correction.

The conclusion is one substantial first-coordinate piece of the
remaining \(R_{44,N}\) product. The real first segment, its negative
vertical join, the first right connections, and completion of the
second period are not inferred.

## 1. Exact source, action and statement

Fix an actual positive three/four word of length \(m\ge4\) beginning
with \(444\). Use the same coupled reference, attached following leg,
and logarithmic lifts as
[the completed central first-plateau theorem](research_mixed_complete44_second_early_central_four.md).
Write \(r_j=a_j+ic_j\), and put
\[
 E=[1/10,11/50],\qquad P=[11/50,9/20],\qquad
 a=x+ic_1,\quad y=q+ic_2,\quad z=u+ic_3,
 \qquad x,q\in E,\quad u\in P.
 \tag{1}
\]
In particular
\[
 -.078<c_1<-.020,\quad -.102<c_2<-.001,\quad
 -.108<c_3,h_s,h_t<-.001,\quad
 .246<a_1<.35,\quad a_2\ge.24.
 \tag{2}
\]
Here \(h_s,h_t\) are the actual heights of the next two conditional
summation indices. The cap's actual private height satisfies
\(-.051<h_e<-.019\). These are bounds on the unchanged reference;
they do not replace its correlations.

With \(r_N=e^{-2\pi i/N}\), retain
\[
 P_j=(r_N;r_N)_j,\quad p_j(V)=(r_NV;r_N)_j,\quad
 X=e^{-2\pi ia},\ Y=e^{-2\pi iy},\ Z=e^{-2\pi iz},
\]
\[
 U_{1,N}(w,X)=\sum_{i<N}H_N(w,r_N^{-i})p_i(X)/P_i^2,\qquad
 C_{1,N}(X,Y)=\sum_{j<N}X^{-j}p_j(X)p_j(Y)/P_j^3.
 \tag{3}
\]
Let \(d_N\) be the original reciprocal-factorial interpolation
polynomial. The exact density is
\[
 \mathscr K_N(w;a,y,z)=
 U_{1,N}(w,X)d_N(X)C_{1,N}(X,Y)d_N(Y)C_{1,N}(Y,Z).
 \tag{4}
\]
There is no first or second selected monomial in (4).
The outgoing allocation is \(|d_N(Z)|^{1/2}\), also at its zeros.

Use precisely the allocated phases
\[
\begin{split}
 \Xi(e,a)&=S(e)+J(e+a)-J(a)-i\pi ea-g(e)-\tfrac12g(a),\\
 F_2(s;a,y)&=g(s+a)+g(s+y)-3g(s)+2\pi ias
                          -\tfrac32g(a)-\tfrac32g(y),\\
 F_3(t;y,z)&=g(t+y)+g(t+z)-3g(t)+2\pi iyt
                          -\tfrac32g(y)-\tfrac32g(z).
\end{split}
 \tag{5}
\]
Thus \(J'(v)=\Log(2\sin\pi v)\), \(J(0)=0\),
\(g(v)=J(v)+i\pi(v-v^2)/2\), with the original branches.
Set \(L_1=\operatorname{stat}_e\Xi\), and let
\(\phi_2,\phi_3\) be the original stationary values of \(F_2,F_3\).
The unchanged three-factor affine action is
\[
 \Lambda_{123}(z)=\Re\{L_1(r_1)+\phi_2(r_1,r_2)+\phi_3(r_2,r_3)
                  +\partial_2\phi_3(r_2,r_3)(z-r_3)\}.
 \tag{6}
\]

**Theorem 1.** On (1), both level parities and a sufficiently small
fixed ordinary-color disk about \(-2\) satisfy
\[
 |\mathscr K_N(w;a,y,z)|\,|d_N(Z)|^{1/2}
 \le C N^B\exp N\{\Lambda_{123}(z)-10^{-12}\}.
 \tag{7}
\]
The same bound holds after integrating in \(a\) on \(E+ic_1\)
with the original density \(N\,da\). Fixed ordinary-color derivatives
obey the estimate on smaller disks with a smaller positive gap.

## 2. The precise old-face profile anchors

For a first ordinary row parameter \(v\), write
\[
 E_1(v;a,y)=I_a(v)+I_y(v)-3J(v)-2\pi c_1v,\qquad
 I_b(v)=\int_0^v\log|1-e^{-2\pi i(b+t)}|\,dt .
 \tag{8}
\]
Its allocated real-row rate is
\[
 \mathcal R_2(v)=E_1(v;a,y)-\tfrac12\Re g(a)-\tfrac12\Re g(y).
 \tag{9}
\]
For a real \(v\) this equals \(\Re F_2(v;a,y)\).
The last rate is
\(\mathcal R_2(1)=-2\pi c_1-\Re g(a)/2-\Re g(y)/2\).
Define \(\mathcal R_3\) in the identical way for \((y,z)\);
its last carrier is \(-2\pi c_2\).

The next complete kernel, with its two half allocations, reduces
to its main, real-low, real-half and last profiles
\[
\begin{split}
 M_3&=\max_{1/8\le t_R\le1/2}\Re F_3(t_R+ih_t;y,z),\\
 L_3&=\Re F_3(1/8;y,z),\qquad
 H_3=\Re F_3(1/2;y,z),\qquad D_3=\mathcal R_3(1).
\end{split}
 \tag{10}
\]
This is the full finite-current reduction in Sections 3--5 of
the central first-plateau theorem: its low block, upper block,
both zero-mode joins, both horizontal aliases and four weighted
vertical halves are included. It holds on the present \(q\in E,u\in P\)
without any change. No first-coordinate variable enters this reduction.

Let
\[
 B_L(x)=\Re L_1(r_1)+\Re L_1'(r_1)(x-a_1)
                  -\kappa_0(x-a_1)^2,\qquad \kappa_0=1/2500000.
 \tag{11}
\]
The proof of the central first-plateau theorem, rather than only
its finite-modulus conclusion, establishes the following raw
profile comparisons for every \(x\in P\):
\[
 B_L(x)+P_2+P_3<\Lambda_{123}(z)-10^{-10}.
 \tag{12}
\]
Here \(P_3\) is any profile in (10), and \(P_2\) is any first
main-line value, either real cut, or its last rate (9).
The main and cut comparisons are Section 3 of that theorem;
the one-last and double-last comparisons are Section 4.
Its Section 5 also bounds each downward cut join by the corresponding
main or real-cut endpoints. All these statements use the two
original marginal cancellations and the same outgoing tangent.
The reserve is supplied by
\(2\kappa_0(a_2-.22)^2\ge1/3125000000>10^{-10}\), or by the
explicit stronger real-cut deficits. No finite upper bound is used
to infer (12).

The [complete cap plane](research_mixed_first_cap_plateau_completion.md)
bounds each of its retained profiles by \(B_L(x)\) on \(P\).
We will use (12) at \(x=.22\), and also at \(x=a_1\) when
retaining the original cap-alias reserve.

## 3. Transport of every main and cut profile

Use the complete early cap source
[at independent fixed heights](research_mixed_cap_early_fixed_height_full_source.md).
Its five regular allocated profiles are \(\Re\Xi(e,a)-p_e\):
the main interval \(e_R\in[.27,.49]\) at height \(h_e\);
the real cuts \(e=.27,.49\); and both alias intervals at heights
\(-.055,.04\), with penalties \(.11\pi,.08\pi\).
Its true-end profile is
\[
 A_{\rm end}(a)=E_{\rm end}-\tfrac12\Re g(a),\qquad
 E_{\rm end}=\frac35+\frac{\log4}{100}<\frac{123}{200}.
 \tag{13}
\]
For type four there is no additional upper-row allowance. These
profiles include all physical cap rows, both zero-mode joins and
all weighted vertical pieces.

Fix \(s=v+i\eta\), \(1/8\le v\le1/2\), \(\eta\le0\).
Writing \(r=e^{2\pi c_1}\), differentiation on the original lift gives
\[
 \partial_x\Re(\Xi+F_2)
 =\log\frac{|1-r e^{2\pi\Im e}e^{-2\pi i(\Re e+x)}|
                 |e^{-2\pi\eta}-r e^{-2\pi i(v+x)}|}
                {|1-r e^{-2\pi ix}|^3}>0.
 \tag{14}
\]
This is equation (9), with its full proof, of
[the complete central cap/neighbor source](research_mixed_early_joint_central_source.md).
Its positivity uses only \(e\in[.27,.49]+i[-.055,.04]\),
\(x\in E\), the first height, \(v\in[1/8,1/2]\), and \(\eta\le0\).
The outgoing target \(y\) is absent from both the derivative
and the proof. Therefore its stated outgoing-plateau restriction
is not used in this transport implication.

Transport each regular cap profile times a first main, real-low,
real-half or downward-cut-join profile to \(x=.22\), with \(q,z\)
and the chosen next profile fixed. The original sampling penalties
are independent of \(x\). Equations (12) and (14) bound every
such product by \(\Lambda_{123}(z)-10^{-10}\).
At \(x=.22\), the needed downward-join comparison is exactly
the one retained in the raw inventory preceding (12); no
vertical convexity is asserted at an early \(x<q\).

For the true cap ends, the combined derivative is instead
\[
 \log\frac{|e^{-2\pi\eta}-r e^{-2\pi i(v+x)}|}
                  {|1-r e^{-2\pi ix}|^2}>-\log2.
 \tag{15}
\]
Indeed \(v+2x\le.94<1\) makes its real-height numerator
larger than a single denominator; increasing \(e^{-2\pi\eta}\)
only increases that numerator. Its denominator is less than two.
The complete transport costs less than
\((3/25)\log2<21/250\).
At \(x=.22\), the original bare cap plane exceeds \(79/100\),
whereas (13) has bare rate below \(123/200\). The allocated
reserve is greater than \(7/40\), by Section 3 of
[the joint low/half proof](research_mixed_early_joint_low_tail.md).
Thus the remaining reserve exceeds \(91/1000\).
This pays (15) before attaching any chosen next profile in (10).
The true ends therefore satisfy the same comparison.

## 4. Every first conditional central correction

For \(s=v+i\eta\), retain the original strip argument
\[
 A(b,\eta)=\arg(1-e^{2\pi\eta-2\pi ib}),\qquad 0<b<1.
\]
Its value lies between zero and \(\pi(1-2b)\).
The imaginary derivative of the first unallocated phase is
\[
 I(v,\eta)=A(v+x,\eta+c_1)+A(v+q,\eta+c_2)
                        -3A(v,\eta)+2\pi x.
 \tag{16}
\]
The outer allocations in (5) are independent of \(s\).
On \(v\in[1/8,1/2]\), \(x,q\in E\), the original argument bounds give
\[
 -11\pi/5<I(v,\eta)<13\pi/10\quad(\eta\in\mathbb R),
 \qquad I(v,\eta)>-77\pi/40\quad(\eta\ge0).
 \tag{17}
\]
Here is the domain check rather than an implicit extension.
For the upper bound,
\[
 I/\pi\le\max(1-2v,2x)+(1-2v-2q)_+\le13/10.
\]
For the lower bound, the four cases for the two shifted real
arguments give
\(-1+2v-2q\), \(-2+4v+2x-2q\), \(-2+4v\),
and \(-3+6v+2x\), all greater than \(-11/5\).
For \(\eta\ge0,v\ge1/5\), the same four expressions exceed
\(-19/10\). For \(v\le1/5\), both \(v+x,v+q<1/2\).
If \(\eta+c_1\ge0\), its first shifted argument is at least
\(\pi(1/2-v-x)\); this gives the lower bound
\(\pi(-5/2+5v+x)\ge-71\pi/40\).
If \(0\le\eta<-c_1\), the own argument is less than \(3\pi/5\):
the proof in Section 4 of the central cap/neighbor source uses
only \(c_1>-.078\), \(v\ge1/8\), and \(e^{2\pi\eta}<5/3\).
Both shifted arguments are nonnegative here, so
\(I>-9\pi/5+\pi/5=-8\pi/5\). This proves (17).

Use exactly the old lower and upper sampling heights \(-1/5,4\).
Since \(h_s\in[-.108,0]\), (17) yields
\[
\begin{split}
 \Re F_2(v-i/5)-2\pi/5
   &<\Re F_2(v+ih_s)-7\pi/50,\\
 \Re F_2(v+4i)-8\pi
   &<\Re F_2(v+ih_s)-39\pi/625.
\end{split}
 \tag{18}
\]
For the second line the total upper cost is less than
\((11/5)(27/250)\pi+4(77/40)\pi-8\pi=-39\pi/625\).
Both weighted vertical halves are bounded by their real cuts:
their outward rate derivatives have the signs
\[
 \partial_\eta(\Re F_2-2\pi\eta)<-3\pi/40\quad(\eta\ge0),
 \qquad
 \partial_\eta(\Re F_2+2\pi\eta)>7\pi/10\quad(\eta\le0).
 \tag{19}
\]
Thus (18)--(19), followed by Section 3, pay every first central
current with every unchanged cap profile and every next profile.
In particular no tall-strip Hessian or positive-height packet is assumed.

## 5. Low rows, full high rows, and the first-last alternative

The exact low-row ratio in
[the original attached low-tail proof](research_mixed_first_attached_low_row_transport.md)
already covers \(x,q\in E\) and the heights (2). Stopping its
geometric-series argument at \(j=\lfloor N/8\rfloor\) bounds
every low physical row, including zero, by \(201\) times the last
row of that block. Its rate is the real-low profile used above.

The [all-angle high-row theorem](research_mixed_complete44_two_early_angles_high_rows.md)
applies because \(c_1\in[-.078,0]\), \(c_2\le0\), and \(x,q\in(0,1/2)\).
It bounds the entire first high block, through \(N-1\), by its
half and last rates. The half rate was paid in Section 3.
It remains to pay \(\mathcal R_2(1)\) with every cap profile.

We use the profile-by-profile proof of
[the first44 last-row calibration](research_mixed_first_four_four_true_last_row_calibration.md).
Its first-coordinate transport and its cap reserves are independent
of the second real angle. The following verifies its remaining
uses of that angle and replaces its old outgoing plane by (12).
Put \(r=e^{2\pi c_1}<9/10\) and \(t=e^{2\pi c_2}>1/2\).

If \(r\le2/3\), its Sections 3--4 prove:

* Every first main and real-cut profile times \(\mathcal R_2(1)\)
  has positive \(x\)-derivative
  \(\log(N_e/D^2)\), with
  \(N_e=|1-r e^{2\pi\Im e}e^{-2\pi i(\Re e+x)}|\) and
  \(D=|1-r e^{-2\pi ix}|\).
  The displayed decreasing cubic and \(P(2/3)=256/16875>0\)
  use no outgoing parameter. Transport to \(x=.22\) and use (12).
* At \(x=a_1\), both full cap aliases have their original
  deficit at least \(3/20\) relative to \(L_1(r_1)\);
  this is Lemma 3 of the
  [complete cap current proof](research_mixed_cap_outer_contour_reduction.md).
  Equation (12), with \(B_L(a_1)=\Re L_1(r_1)\), attaches the
  first last rate and every next profile without changing that
  deficit. The possible transport loss back to \(x\in E\) is
  less than \(46/1875+1/15+1/20\), by the same three intervals
  and radial inequalities in the last-row proof. A reserve
  greater than \(11/1250\) remains.
* The true-end profile has derivative \(-\log D>-23/225\).
  Its loss from \(x=.22\) is less than \(23/1875\), paid from
  the same \(7/40\) true-end reserve, leaving more than \(1/10\).

If \(r\ge2/3\), the radial comparison in that proof gives, for
\(4/25\le x\le11/50\),
\[
 \mathcal R_2(1/2)-\mathcal R_2(1)
     =\mathcal S_r(x)+\mathcal S_t(q)+\tfrac12\log r>1/72.
 \tag{20}
\]
Here \(\mathcal S_t\) is symmetric about \(1/4\), increasing
up to \(1/4\), and increasing in its radius. Its old lower bound
\(\mathcal S_t(q)>\mathcal S_{1/2}(1/20)\) remains valid since
now \(1/10\le q\le11/50<1/4\). Thus all written witnesses
for (20) apply unchanged, with a stronger outgoing angular bound.
Section 3 pays the half rate, hence also the last rate.
For \(x\le4/25\), every regular cap profile times the last
rate has \(N_e>1,D^2<1\), and its derivative is positive;
the true-end derivative \(-\log D\) is positive as well.
Transport to \(x=4/25\) completes this case.

In every case, the chosen next profile is independent of \(x\).
All first-last comparisons consequently retain the raw gap
in (12). This includes the first-last/next-last alternative,
whose anchor at \(x\in P\) is the double-last proof in the
central first-plateau theorem.

## 6. Exact finite completion and scope

Split the first conditional sum into exactly
\[
 0\le j\le\lfloor N/8\rfloor,\qquad
 \lfloor N/8\rfloor+1\le j\le\lceil N/2\rceil-1,\qquad
 \lceil N/2\rceil\le j<N.
 \tag{21}
\]
For its middle block use the exact marked factorial interpolant
and half-grid cotangent formula retained in Section 6 of the
central cap/neighbor source. The contour is
\([\ell_N,u_N]+i[-1/5,4]\), with
\(\ell_N=(\lfloor N/8\rfloor+1/2)/N\) and
\(u_N=(\lceil N/2\rceil-1/2)/N\).
The constant cotangent modes give \(+N\) times the real integral.
Moving only that zero mode to \(h_s\) leaves both unweighted joins.
The remaining modes give two horizontal aliases and four weighted
vertical halves. Sections 3--4 pay all of them.
Here both shifted real arguments lie in \([.225,.72]\) in the
limiting rectangle, so the original regular factorial symbol
and its logarithmic lift remain valid throughout every fixed
height used. Half-grid shifts are absorbed in the source tolerance.

Section 5 pays both complete physical blocks. The next kernel
is reduced by the already complete source (10), retaining its
main density, all eight complementary paths and both physical blocks. The
complete cap source retains all its rows, cuts, joins and aliases.
At every step the allocation is precisely (5): each internal
halfweight occurs twice, giving \(d_N(X)\) and \(d_N(Y)\),
and only the original outgoing half at \(Z\) remains.
The [Fourier-weight theorem](research_mixed_fourier_weight_continuation.md)
supplies these full polynomial upper rates at their actual negative
heights; no finite Fourier value or halfweight is divided out.

Each raw product has the common gap \(10^{-10}\), with larger
reserves in the true-end and alias comparisons. Choose all finitely
many symbol, endpoint, color and half-grid allowances below a
common fraction of that gap. All path lengths, finite row counts
and original cotangent densities contribute polynomial factors.
This proves (7), including every literal row and both parities.
The cap's zero-safe all-real coefficient bounds and degree continuation,
or the fixed color neighborhoods in the same sources, give a fixed
ordinary-color disk after this allowance is chosen. Cauchy estimates
give the stated color derivatives on smaller disks.

Integration over \(E+ic_1\) costs only its fixed length and the
original factor \(N\). It therefore pays exactly the unselected
early first horizontal in the \(R_{44,N}\) decomposition. No
substantial first-height change, real first endpoint, selected
first current or first right connection has been included.
The entire \(R_{44,N}\) and full second-period comparisons remain
separate from this theorem.

## Direct source versions

| Source | SHA-256 |
|---|---|
| research_mixed_complete44_second_early_central_four.md | e5be8082613eac6887d3aca857703e4ac5b511c430f35ca91fa388c71a924f45 |
| research_mixed_early_joint_central_source.md | f19a7b5c42a4f372e9671c95dec5670f501065802fa96279b542efaa5005aec3 |
| research_mixed_early_joint_low_tail.md | 72ee3edebe390f213751e7774913d7d6552d6eff3bdea61b13f4d23159ad6606 |
| research_mixed_first_four_four_true_last_row_calibration.md | 52c149d8500e88c6e4e3fdf1c9e699baf376dfaac8b96d3461dc81f9d1725e0d |
| research_mixed_cap_early_fixed_height_full_source.md | d930407eaa5a0bb7c735ee9521c6d352f637124c57c5593cbb1813f069f7d423 |
| research_mixed_first_attached_low_row_transport.md | 8ef728d3808e1480d85a81c1ed8f7eebda99392d0b11f1262e4a47b5a2b196d3 |
| research_mixed_complete44_two_early_angles_high_rows.md | b088d7b6e388f65f3a96e9176f810cfd0936cb31f425e47fcd9808c6dcb81c8d |
| research_mixed_fourier_weight_continuation.md | 0bae41d83f414eb91fd137de1242120a11408147d56ec752e466ca5ed7e7f48e |
| research_mixed_first_cap_plateau_completion.md | 4b1a55000a114835ce4b2868b79f4bec63ee781d6d997f7fa6b37f7896e4e87d |
| research_mixed_cap_outer_contour_reduction.md | 52bd01353c084aa8bb8d74a1abd015c0cfebdbe6a796c8958bb8796aaba0f9b4 |

Author full proof readback and all ten directly used source implications
and hash checks are complete. Independent full proof/direct-source
review is required before adoption. No mathematical numerical evaluation,
saved-value arithmetic, test, import, compilation or frozen-source edit
is used.
