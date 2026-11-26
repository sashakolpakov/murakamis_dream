# The complete selected first-four/four source at its zero-height left face

Private written proof, 10 November 2026. At the first real coordinate
one tenth and height zero, the original selected first-four/four
product has a strict gap below the same geometric affine rate as its
positive-height theorem. The comparison retains each coherent cap
profile before taking any maximum. An integrated horizontal gain pays
the height reset; the old absolute collar ceiling is not used.

This is a bound at one outer face. It does not itself estimate the
outer vertical segment joining that face to positive height.

## 1. Actual reference, source and statement

Fix an actual positive three/four open word of length at least three
beginning with four and four. Retain its coupled reference, branches
and normalization from the
[complete selected early source](research_mixed_selected_four_four_early_complete_source.md).
In particular
\[
 h_e\in[-.051,-.019],\qquad h_s,d\in[-.102,-.001].
\tag{1}
\]
The reference remains actual throughout; these containing intervals
are used only for uniform inequalities. Set
\[
 x_-=1/10,\quad x_+=11/50,\quad H=1/100,\qquad
 a=x+ih,\quad b=z+id,\quad z\in P=[11/50,9/20].
\tag{2}
\]
The conclusion is at \(a=x_-\). Intermediate targets in the proof
have \(x\in[x_-,x_+]\), \(0\le h\le H\), with \(b\)
fixed. No other reference height is moved.

For \(q_N=e^{-2\pi i/N}\), put
\[
 P_j=(q_N;q_N)_j,\quad p_j(X)=(q_NX;q_N)_j,\quad
 X=e^{-2\pi ia},\quad Y=e^{-2\pi ib}.
\]
Retain exactly
\[
\begin{split}
 U_{1,N}(w,X)&=\sum_{i=0}^{N-1}
             \frac{H_N(w,q_N^{-i})p_i(X)}{P_i^2},\\
 C_{1,N}(X,Y)&=\sum_{j=0}^{N-1}R_{j,N}(a,b),\qquad
 R_{j,N}=X^{-j}\frac{p_j(X)p_j(Y)}{P_j^3},\\
 \mathcal K_N(w;X,Y)&=U_{1,N}(w,X)C_{1,N}(X,Y)d_N(X)X^{-N}.
\end{split}
\tag{3}
\]
Here \(H_N\) is the complete original cap coefficient. The outgoing
allocation is \(|d_N(Y)|^{1/2}\), not a holomorphic square root.
The first factor is the whole \(d_N(X)X^{-N}\), even though
\(|X^{-N}|=1\) at the face in question.

Use the same original bare phases
\[
\begin{split}
 \Psi(e,a)&=S(e)+g(e+a)-g(a)-g(e)-\frac{i\pi}{2}(e-e^2),\\
 Q(s;a,b)&=g(s+a)+g(s+b)-3g(s)-g(a)-g(b)+2\pi ias,\\
 \mathcal F&=\Psi+Q-g(a)-\tfrac12g(b),\\
 M&=\Re\mathcal F(e_*,s_*;a_*,b_*),\quad
 p=\mathcal F_b(e_*,s_*;a_*,b_*),\\
 \Lambda(z)&=M+\Re p\,(z-\Re b_*).
\end{split}
\tag{4}
\]
In particular the outgoing affine term and every additive constant
are unchanged.

**Theorem 1.** At \(a=1/10\), for every \(\tau>0\) and both
level parities,
\[
 |\mathcal K_N(w;X,Y)|\,|d_N(Y)|^{1/2}
 \le C_\tau N^{A_\tau}
             e^{N\{\Lambda(z)-1/1000+\tau\}}
\tag{5}
\]
uniformly for \(z\in P\) and every real ordinary color
\(w\in[-2,2]\). On a sufficiently small fixed ordinary-color
disk about \(-2\), the same rate holds, and every fixed color
derivative has this bound on a smaller disk with polynomial cost.
Every finite row and every cap and ordinary contour correction is
included.

The proof first gives a stronger profile statement needed when this
face is used as an endpoint of a later contour.

## 2. The retained profiles and their positive-height calibration

Keep the five cap profiles
\[
\begin{array}{ll}
 A_0(a)=\max_{.27\le u\le.49}\Re\Psi(u+ih_e,a),&
 A_L(a)=\Re\Psi(.27,a),\quad A_R(a)=\Re\Psi(.49,a),\\
 A_-(a)=\max_u\Re\Psi(u-.055i,a)-.11\pi,&
 A_+(a)=\max_u\Re\Psi(u+.04i,a)-.08\pi.
\end{array}
\tag{6}
\]
Their respective private points all belong to
\([.27,.49]+i[-.055,.04]\). The sixth, true-end profile is
\[
 A_*(h)=\frac35+2\pi h+\frac{\log4}{100},
                         \qquad 0\le h\le H.
\tag{7}
\]
The [complete independent-height cap theorem](research_mixed_cap_early_fixed_height_full_source.md)
applies on the entire proof rectangle, including \(h=0\).
For own type four its extra upper-row allowance is exactly zero.
It retains both zero-mode joins, both horizontal aliases, all four
vertical alias halves, the full compact physical tails and the true
ends. Discarding its favorable ordinary-color angular loss gives
the maximum of (6)--(7) uniformly for all real colors.

Include the outgoing half allocation in the ordinary profiles:
\[
\begin{split}
 B_0(a,b)&=\max_{1/8\le v\le1/2}
                \Re Q(v+ih_s;a,b)-\tfrac12\Re g(b),\\
 B_L(a,b)&=\Re Q(1/8;a,b)-\tfrac12\Re g(b),\\
 B_R(a,b)&=\Re Q(1/2;a,b)-\tfrac12\Re g(b),\\
 W(a)&=-\Re g(a)-2\pi h.
\end{split}
\tag{8}
\]
At \(a_+=x_++iH\), equation (27) of the complete selected
early source gives the individual comparisons
\[
 A_i(a_+)+B_j(a_+,b)+W(a_+)
       \le\Lambda(z)-1/2000,
 \quad i\in\{0,L,R,-,+,*\},\quad j\in\{0,L,R\}.
\tag{9}
\]
These are profile inequalities proved before summing the finite
source, rather than an inference from cancellation of a whole kernel.

We shall prove
\[
 A_i(x_-)+B_j(x_-,b)-J(x_-)
       <\Lambda(z)-1/1000
 \quad(i\in\{0,L,R,-,+,*\},\ j\in\{0,L,R\}),
\tag{10}
\]
where \(J(x)=\Re g(x)\) on the real interval. All cap penalties
in (6) remain part of this comparison.

## 3. An integrated gain along the real first coordinate

Fix any one of the regular cap private points
\(e=u+i\xi\) in (6), with its prescribed penalty, and fix an
ordinary main point \(s=v+ih_s\) or one of its two real cuts.
Write \(\eta=\Im s\le0\). At incoming height zero put
\[
 R=e^{2\pi\xi},\quad q=e^{-2\pi\eta}\ge1,\quad
 D(x)=2\sin\pi x,
\]
\[
 N_e(x)=|1-R e^{-2\pi i(u+x)}|,\qquad
 N_s(x)=|q-e^{-2\pi i(v+x)}|.
\tag{11}
\]
Exact differentiation of (4), including its chirps, gives
\[
 \partial_x\Re\mathcal F(e,s;x,b)
                   =\log\frac{N_e(x)N_s(x)}{D(x)^3}.
\tag{12}
\]
The fixed cap alias penalty has zero derivative.

The following bounds hold over the whole fixed private intervals;
there is no restriction to a moving maximizer. First \(R>7/10\).
Indeed \(.11\pi<7/20\), and the positive exponential-series bound
\[
 e^t\le1+t+\frac{t^2}{2(1-t/3)}
\]
at \(t=7/20\) is \(3009/2120<10/7\). Also
\(u+x\in[.37,.71]\), where
\(\cos2\pi(u+x)<-6/25\). At its larger endpoint cosine,
use \(\sin(2\pi/25)>\sin(1/4)>95/384>6/25\);
the other endpoint cosine is smaller. Consequently
\[
 N_e^2>1+\frac{49}{100}+\frac{12}{25}\frac7{10}
       =\frac{913}{500}>\frac95.
\tag{13}
\]
The ordinary sum lies in \([.225,.72]\), on which
\(\cos2\pi(v+x)<1/6\): its largest cosine is
\(\cos(.45\pi)=\sin(\pi/20)<11/70<1/6\).
Thus
\[
 N_s^2>q^2+1-q/3\ge5/3,\qquad N_e^2N_s^2>3.
\tag{14}
\]

The function \(x\mapsto\log(2\sin\pi x)\) is strictly
concave. Its mean on \([1/10,11/50]\) is therefore at most
its value at the midpoint \(4/25\). The elementary estimate
\[
                    2\sin(4\pi/25)<49/50
\tag{15}
\]
has the following written witness. For \(0<t<1\), the alternating
sine series gives \(\sin t<t-t^3/7\). The latter polynomial
increases on this interval. Since
\(4\pi/25<88/175<101/200\), its value is at most
\[
 \frac{101}{200}-\frac1{7}\left(\frac{101}{200}\right)^3
       =\frac{27249699}{56000000}<\frac{49}{100}.
\]
The sine-series assertion follows from
\(1/6-t^2/120>19/120>1/7\).

Integrating (12), using (13)--(15), proves
\[
 \Re\mathcal F(e,s;x_+,b)-\Re\mathcal F(e,s;x_-,b)
 >\frac3{50}\log3+\frac9{25}\log(50/49)>\frac7{100}.
\tag{16}
\]
For the last strict inequality, the positive atanh series gives
\(\log3>1+1/12=13/12\), and integration of \(1/t\) on
\([49,50]\) gives \(\log(50/49)>1/50\). Their contribution
is \(13/200+9/1250=361/5000>7/100\).

## 4. The selected-height reset at the old face

At \(x=x_+\), vary only the incoming height \(h\) from zero
to \(H\), retaining the same private points as in Section 3.
Let
\[
 \mathcal A(t,y)=\arg(1-e^{2\pi y-2\pi it})
\]
be the original regular-strip argument. It is continued from height
zero, with no independent logarithmic reset. For \(h\ge0\),
\[
 \mathcal A(x_+,h)\ge7\pi/25.
\tag{17}
\]
At every finite height, an argument with real part \(t<1/2\)
is at most \(\pi(1-2t)\), and one with \(t\ge1/2\) is
nonpositive. Since \(u+x_+\in[.49,.71]\), this gives
\[
 \mathcal A(u+x_+,\xi+h)\le\pi/50.
\tag{18}
\]
For the ordinary point, split according to \(v+x_+<1/2\).
In that case
\(\mathcal A(v+x_+,\eta+h)+2\pi v\le14\pi/25\);
in the other case it is at most \(2\pi v\le\pi\).
Thus throughout the full private interval
\[
             \mathcal A(v+x_+,\eta+h)+2\pi v\le\pi.
\tag{19}
\]
Directly from the original phase,
\[
\begin{split}
 \partial_h\{\Re\mathcal F(e,s;x_++ih,b)-2\pi h\}
 ={}&3\mathcal A(x_+,h)-\mathcal A(u+x_+,\xi+h)\\
   &-\mathcal A(v+x_+,\eta+h)-2\pi v-2\pi
 \ge{}&-109\pi/50.
\end{split}
\tag{20}
\]
Combining (16) and (20) shows, pointwise before any maximum,
\[
 \Re\mathcal F(e,s;x_-,b)
 <\Re\mathcal F(e,s;a_+,b)-2\pi H
                 -\frac7{100}+\frac{109\pi}{5000}.
\tag{21}
\]
Here
\[
 \frac7{100}-\frac{109\pi}{5000}>\frac{13}{8750}>\frac1{2000},
\tag{22}
\]
using \(\pi<22/7\). The cap penalties are identical at the two
ends. Maximizing only after (21) and applying (9) proves (10)
for every regular cap profile. Neither uniqueness nor differentiability
of a profile maximizer is required.

## 5. The true cap ends

For a fixed ordinary main point or real cut define
\[
 T(x,h;s,b)=A_*(h)+\Re Q(s;x+ih,b)
                       -\tfrac12\Re g(b)-\Re g(x+ih)-2\pi h.
\tag{23}
\]
At height zero its exact horizontal derivative is
\(\log(N_s/D^2)\). Equations (14)--(15) give
\[
 T(x_+,0;s,b)-T(x_-,0;s,b)
 >\frac3{50}\log(5/3)+\frac6{25}\log(50/49)>\frac3{100}.
\tag{24}
\]
Here \(\log(5/3)>1/2\) follows from the positive atanh series
with argument \(1/4\).

The \(+2\pi h\) in the literal true-end ceiling (7) cancels
the selected monomial's rate. Hence at \(x=x_+\),
\[
 \partial_h T=2\mathcal A(x_+,h)
              -\mathcal A(v+x_+,\eta+h)-2\pi v
                    \ge-11\pi/25.
\tag{25}
\]
The reset costs at most \(11\pi/2500\). Since
\(3/100-11\pi/2500>1/2000\), equations (9), (24)--(25)
prove (10) also for \(A_*\). No regular asymptotic is used at a
true cap endpoint.

## 6. The full finite ordinary factor at height zero

The cap theorem already accounts for every cap current and row.
For the ordinary sum in (3), keep the disjoint partition
\[
 \begin{array}{ll}
 0\le j\le\lfloor N/8\rfloor,&\text{low},\\
 \lfloor N/8\rfloor+1\le j\le\lceil N/2\rceil-1,&\text{central},\\
 \lceil N/2\rceil\le j<N,&\text{high}.
 \end{array}
\tag{26}
\]
The [literal low-row recurrence](research_mixed_first_attached_low_row_transport.md)
allows incoming height zero and the full outgoing range (1).
Every step up to \(N/5\) has modulus ratio greater than
\(e^{1/200}\); the low block in (26) is therefore below 201
times its final row. Its continuous allocated rate is \(B_L\),
with the original rounding tolerance. This covers \(j=0\).

For the central block use the original marked factorial interpolation,
half-grid cuts tending to \(1/8,1/2\), lower height \(-1/5\)
and upper height \(2\). All real factorial arguments stay inside
the compact regular strips
\[
 s+a:\ [.225,.6],\qquad s+b:\ [.345,.95],\qquad
 s:\ [1/8,1/2].
\tag{27}
\]
The [exact factorial theorem](exact_factorial_interpolation_and_complex_contours.md)
allows these fixed finite heights. The same exact residue formula
as the [asymmetric-contour proof](research_mixed_horizontal_asymmetric_contour.md)
has coefficient \(N/(2i)\), gives zero-mode density \(+N\),
and retains both horizontal aliases and all four vertical alias halves.
No factorial pole is crossed. Move only its zero mode to \(h_s\).

For completeness, the own-four argument estimates in Section 5 of
the selected early source remain valid at incoming height zero.
The real ranges and ordering \(x\le z\) are unchanged. The only
positive-height lower estimate used there is
\[
 \mathcal A(v+x,y+h)\ge\pi(1/2-v-x)
               \quad(y\ge0,\ h\ge0,\ v+x<1/2),
\]
which includes \(h=0\). With \(I=\Im Q_s\), the resulting
uniform bounds are
\[
 I\le53\pi/50,\qquad
 I\ge-43\pi/40\ (y\le0),\qquad
 I\ge-77\pi/40\ (y\ge0).
\tag{28}
\]
Consequently the lower and upper horizontal aliases are below the
same actual main point by at least
\[
                         47\pi/250,\qquad339\pi/10000,
\tag{29}
\]
respectively. The upper weighted vertical derivative is at most
\(-3\pi/40\), and the lower weighted derivative at least
\(47\pi/50\). Every vertical alias half is therefore bounded by
its real-cut endpoint. These are finite-height bounds; no alias is
sent to infinity.

The unweighted joins only use index heights in \([h_s,0]\).
Their vertical convexity holds down to the same left cut. Here is
a direct check at the present incoming face. Put
\[
 U=\Re\cot\pi s,\quad C=\Re\cot\pi(s+x_-),\quad
 C_b=\Re\cot\pi(s+b),\quad u_0=\cot\pi v.
\]
The height inequality (8) of the
[early central theorem](research_mixed_selected_four_four_early_central.md)
gives \(U>u_0/2\) for \(v<1/2\), throughout the enlarged
join range \([-.108,0]\). If \(C>0\), then
\(C\le\cot\pi(v+x_-)<u_0<2U\); if \(C\le0\),
the same positivity of \(2U-C\) is immediate. Likewise
\(U-C_b>0\): when \(C_b>0\), put \(p_b=\cot\pi z<4/3\)
and use
\[
 C_b\le\frac{u_0p_b-1}{u_0+p_b}<u_0/2<U,
\]
because \(u_0^2-p_bu_0+2>0\). These are the same elementary
guards as in that central theorem. At \(v=1/2\), \(U=0\)
and both shifted real cotangents are negative. Thus
\[
 -\Re Q_{ss}/\pi=(2U-C)+(U-C_b)>0.
\tag{30}
\]
Holomorphy makes every zero-mode join vertically convex, hence bounded
by its main and real endpoints. Equations (10), (28)--(30) now pay
every central term after multiplication by the complete cap.

For the high block the exact reflected drift is zero, including
the incoming equality case:
\[
                       2\pi\{(-0)_++d_+\}=0.
\tag{31}
\]
The [all-angle high-row theorem](research_mixed_all_angle_high_row_sign_class.md),
Theorem 2 and Corollary 3, explicitly includes zero heights. With
own flag one it gives the full zero-safe bound
\[
 \sum_{j=\lceil N/2\rceil}^{N-1}|R_{j,N}(x_-,b)|
       \le C_\tau N^{A_\tau}e^{N\{E_1(1/2;x_-,b)+\tau\}}.
\tag{32}
\]
The continuous half rate, with the outgoing half allocation, is
exactly \(B_R\). This includes all wrapped rows, numerator zeros,
revived rows and the stop \(N-1\), at both parities. It is not a
comparison to a possibly zero finite half-row value.

Finally the [whole Fourier polynomial theorem](research_mixed_fourier_weight_continuation.md)
gives upper rate \(\max\{-J(x_-),0\}=-J(x_-)\) for the
literal selected first weight at height zero. The last equality
uses \(J(x_-)<0\). The outgoing height is negative, so its
unchanged modulus half allocation has rate \(-\Re g(b)/2\).
There is no division by either finite Fourier factor. Combining
(10) with the three blocks (26), all symbols, both \(+N\)
current densities and all half-grid errors proves (5), with one
arbitrarily small total tolerance and polynomial factors.

The cap bound is uniform on the whole real ordinary-color interval;
all other factors are color independent. The literal product has
degree less than \(N\) in that color. Interval polynomial
continuation therefore supplies a fixed disk at any prescribed
additional rate allowance. Cauchy's formula on a smaller disk gives
all fixed derivatives. At a zero of a common multiplier the bound
is immediate, so continuation uses no division.

## 7. The unreduced current-profile conclusion

We state the endpoint input explicitly, before taking the final
finite-sum modulus. At \(a=x_-\), let \(\mathscr B\) consist of
the following individual rates, each with the same outgoing term
\(-\Re g(b)/2\):

* \(\Re Q(s;a,b)\) on the actual main horizontal interval, both
  real cuts, and both zero-mode joins between height \(0\) and \(h_s\);
* \(\Re Q(s;a,b)-2\pi|\Im s|\) on both horizontal aliases at
  heights \(-1/5,2\), and on all four vertical alias halves at
  either real cut;
* \(E_1(t;a,b)\) at every physical-tail rate parameter
  \(t\in[0,1/8]\cup[1/2,1]\), including the literal endpoint rate
  \(E_1(1;a,b)=0\).

The inequalities in Section 6 prove, separately for every member,
\[
                 B\le\max\{B_0,B_L,B_R\}\qquad(B\in\mathscr B).
\tag{33}
\]
For the low continuous interval this is the derivative form of the
same exact low-row lemma; for the high interval it is Theorem 2 of
the all-angle source, including all its equality-height limits.
The original finite aliases have their exact signs and cotangent
denominators, whose bounded or polynomial costs do not change
the rates displayed here.

**Proposition 2.** For every cap profile or true-end alternative
\(i\in\{0,L,R,-,+,*\}\), every \(B\in\mathscr B\), and both
whole selected Fourier upper alternatives \(W_1=-J(x_-)\), \(W_0=0\),
\[
                    A_i(x_-)+B+W_\nu
                          <\Lambda(z)-1/1000,\qquad \nu=0,1.
\tag{34}
\]
Indeed (33) and (10) give this for \(W_1\), and \(W_0<W_1\).
All cap profile maxima are independent of the ordinary private
point, so this pays their Cartesian product. The corresponding
individual cap zero-mode joins and vertical alias halves are
also included: the complete cap theorem bounds each of those raw
rates by its main, real-cut or horizontal-alias endpoints in (6).
Thus (34) applies to every retained cap current, as well as its
separate true-end sector, times every raw ordinary current after
the exact penalties and allocations. It is stronger than a bound
on the modulus of a cancelling whole product.

This profile statement is available as an endpoint input. This
note proves neither the outer height-changing join nor the remaining
first-coordinate period. It asserts no whole-word noncancellation,
new knot family or short-partial-filling theorem.

## Direct source versions

| Source | SHA-256 |
|---|---|
| research_mixed_selected_four_four_early_complete_source.md | 760ab93cc36ccba00eea97c518eb3697f55638b90c43c90d5ce1a9cd029ddc05 |
| research_mixed_cap_early_fixed_height_full_source.md | d930407eaa5a0bb7c735ee9521c6d352f637124c57c5593cbb1813f069f7d423 |
| research_mixed_first_attached_low_row_transport.md | 8ef728d3808e1480d85a81c1ed8f7eebda99392d0b11f1262e4a47b5a2b196d3 |
| research_mixed_all_angle_high_row_sign_class.md | 3a959f0a6bb064767e753e90061a2d9ef323268e79cbdf19c1043a6fe9691144 |
| research_mixed_selected_four_four_early_central.md | 7ed3ce53e89313ee0b149c4901a3eb29de7011462aa2d928346db1f233939b48 |
| exact_factorial_interpolation_and_complex_contours.md | 1f34f65437dfe0bfb4062a7a74840beae1676353cf13bb8a86f8849a8a36bc72 |
| research_mixed_horizontal_asymmetric_contour.md | 2b0984562d9d3c63e2e366d9dc3b68f557512b71c74290f8ac530fcb4d3e7fce |
| research_mixed_fourier_weight_continuation.md | 0bae41d83f414eb91fd137de1242120a11408147d56ec752e466ca5ed7e7f48e |

Only written inequalities and source/hash inspection were used. No
mathematical numerical evaluation, saved-value arithmetic, import,
test, compilation or frozen-source edit was performed.
