# Attaching the complete type-three kernel at actual cap-343 heights

Private research proof candidate, 8 November 2026. The actual
type-three window heights improve the bounded-prefix attachment
enough to cover the cap-initialized family with \(7/10<R<41/50\).
This is a new source theorem candidate, separate from the central
first-factor assembly. It requires full source and proof reviews
before adoption. No numerical evaluation or frozen-source edit
is used.

## 1. Source, actual heights and statement

Use the original ordinary-next reference beginning \(343\), its
fixed heights, \(g\), and \(\Lambda_{123}(z)\), exactly as in
[the earlier bounded-prefix theorem](research_mixed_next_three_deep_radius_bounded_prefix.md).
Put
\[
\begin{gathered}
y=q+ih_y,\quad 0\le q\le q_0=11/50,\qquad
z=u+ih_z,\quad u\in P=[11/50,9/20],\\
R=e^{2\pi h_y},\qquad \rho=e^{2\pi h_z},\qquad
A=e^{-2\pi h_t},\\
\frac7{10}\le R\le\frac{41}{50},\qquad
-\frac3{100}<h_t,h_z<\frac1{50}.
\end{gathered}
\tag{1}
\]
Here \(h_t=\Im s_3^*\) is the original next private height
and \(h_z=\Im t_3^*\) is its outgoing height. All other actual
reference correlations and the original marginal allocation
remain imposed. In particular no arbitrary independent choice
of heights is being substituted for an actual reference.

For every actual complete word in the original powers three
and four, beginning \(343\), with length \(m\ge5\), (1) follows
from [the correlated height theorem](research_mixed_cap_343_correlated_height_bounds.md)
and the type-three row at \(j=3\) of
[open-window inheritance, Theorem 1](research_mixed_open_word_window_inheritance.md).
The latter supplies both private and outgoing heights.
It gives the useful exact bounds
\[
                 \frac45<\rho<\frac87,\qquad A>\frac78 .
\tag{2}
\]
For the lower bound use
\(3\pi/50<33/175<2/9<\log(5/4)\).
For the upper bounds use
\[
                  \frac{\pi}{25}<\frac{22}{175}
                              <\frac2{15}<\log\frac87.
\tag{3}
\]
Both logarithmic inequalities follow from
\(\log x>2(x-1)/(x+1)\), \(x>1\).
Theorem 1 of the correlated-height note applies already at
\(m=4\); the two height refinements in (1) used here require
\(m\ge5\). Terminal \(343\) is not included.

Let \(r=e^{-2\pi i/N}\), \(P_j=(r;r)_j\), and
\(p_j(W)=(rW;r)_j\). The literal next kernel and Fourier weight are
\[
C_{0,N}(Y,Z)=\sum_{j=0}^{N-1}
             \frac{Y^{-j}p_j(Y)p_j(Z)}{P_j^2},
\quad
Y=e^{-2\pi iy},\quad Z=e^{-2\pi iz},\quad
d_N(r^b)=P_b^{-1},\quad\deg d_N\le N-1 .
\tag{4}
\]
The whole finite polynomial \(d_N\), including its forcing,
is retained. There is no next outgoing halfweight.

Set \(B_0=2383/1500\). Suppose that the preceding factor \(V_N\)
satisfies, uniformly on the stated domain, for every \(\tau>0\),
\[
                  |V_N|\le C_\tau N^{B_\tau}
                                    e^{N(B_0+\tau)}.
\tag{5}
\]
It may depend on other variables, but those variables must not
change the actual reference or its action.

**Theorem.** Under (1), (5), and the original reference hypotheses,
the complete finite source obeys, at both level parities,
\[
\boxed{\quad
 |V_Nd_N(Y)C_{0,N}(Y,Z)|
       \le C N^B e^{N\{\Lambda_{123}(z)-1/200\}}.
\quad}
\tag{6}
\]
No holomorphy of \(V_N\) is needed for this pointwise statement.
Outside derivatives require their own neighborhood hypotheses.

## 2. Boundary calibration and the exact profiles

Write
\[
\begin{split}
Q_0(t;y,z)&=g(y+t)+g(z+t)-2g(t)-g(y)-g(z)+2\pi iyt,\\
E(t;y,z)&=\int_0^t\log|1-Ye^{-2\pi ib}|\,db
          +\int_0^t\log|1-Ze^{-2\pi ib}|\,db
          -2J(t)-t\log R,\\
L_0&=-\log R+\log_+\rho,\qquad \log_+\rho=\max(0,\log\rho).
\end{split}
\tag{7}
\]
The original carrier is present in both rates.
The last physical rate is \(L_0\), including positive outgoing
height when it occurs.

Section 2 of the earlier bounded-prefix theorem derives,
before imposing its deeper-radius transport restriction, the
following \(q=q_0\) profile calibration:
\[
\begin{split}
B_0+\Re Q_0(t;y,z)-\Re g(y)&<\Lambda_{123}(z)-1/50,\\
B_0+L_0-\Re g(y)&<\Lambda_{123}(z)-1/50 .
\end{split}
\tag{8}
\]
The first line covers the original next main profiles and the
real low and half cuts \(3/20,1/2\).
Every real upper row at \(q_0\) also satisfies this bound,
by its original half/last profile reduction.
These are individual profile estimates from
[ordinary source assembly, Sections 1--2](research_mixed_three_row_source_assembly.md),
not estimates extracted from a coherently bounded sum.

For precision, the two marginal reserves are those of
[the original low-block theorem, equations (9)--(10)](research_mixed_conditional_lower_output_low_block.md):
\[
\frac74-B_0-\frac{11}{80}=\frac{143}{6000}>\frac1{50},
\qquad
\frac74+\frac1{45}-B_0-\frac1{12}-\frac{801}{10000}
                  =\frac{1811}{90000}>\frac1{50}.
\tag{9}
\]
They retain the original plane slope and action.
They have no hypothesis \(R\le7/10\).

## 3. Main profiles, real low cut and real half cut

The original own-three lower clipping increases a main profile
from real index \(3/20\le t_R<1/6\) to \(1/6+ih_t\).
This is the next clipping of
[the joint-profile theorem, Section 3](research_mixed_next_lower_left_joint_main_profiles.md);
it allows either sign of \(h_t\).
Retain the full remaining main range \(1/6\le t_R\le1/2\).
No own-four upper clipping is used.

For \(\mathcal A=B_0+\Re Q_0-\Re g(y)\), the exact derivative is
\[
\partial_q\mathcal A
 =\log|A-Re^{-2\pi i(q+t_R)}|-\log D_q,\qquad
D_q=|1-Y|^2.
\tag{10}
\]
The real low cut uses the same formula with \(t_R=3/20,A=1\).

On \(q\le1/10\), \(\cos2\pi q>4/5\), and convexity in \(R\)
gives \(D_q<9/20\). For a main, the shifted cosine is at most
\(1/2\), so its numerator is at least
\(\sqrt3 A/2>7\sqrt3/16>3/4\).
The last comparison follows from \(\sqrt3>12/7\).
For the real low cut, \(\cos(3\pi/10)<3/5\) gives numerator
greater than \(4/5\). Thus (10) is positive for both profiles.

On \(1/10\le q\le3/20\), the shifted cosine is nonpositive.
The main numerator square is greater than
\(49/64+49/100>1\), and the real low cut is stronger.
Since \(\cos2\pi q>7/12\), convexity gives
\[
D_q<\max\{101/150,1342/1875\}<3/4 .
\tag{11}
\]
Both derivatives are again positive.

On the last two intervals use the bounds
\[
\begin{array}{c|c|c}
q\text{ interval}&D_q\le D(R)&
|A-Re^{-2\pi i(q+t_R)}|^2>U(R)\\ \hline
[3/20,1/5]&1+R^2-3R/5&
49/64+R^2+21R/40\\
[1/5,11/50]&1+R^2-9R/25&
49/64+R^2+63R/200 .
\end{array}
\tag{12}
\]
The same bounds apply to the real low cut.
The shifted cosine upper bounds are \(-3/10,-9/50\), and
the unshifted cosine lower bounds are \(3/10,9/50\).
These are the original pentagon and
\(\sin(3\pi/50)>9/50\) witnesses used in Section 3 of the
earlier bounded-prefix theorem. Here the improved \(A>7/8\)
gives the displayed \(U\).

We verify \(U>D^2\) in the first row and
\(U>(81/100)D^2\) in the second.
For \(D=1+R^2-dR\), \(d=3/5\) or \(9/25\),
\[
(D^2)''=12(R-d/2)^2+4-d^2\ge139/25
                     \quad(7/10\le R\le41/50).
\tag{13}
\]
Since \(U''=2\), both differences are strictly concave.
The following rational endpoint witnesses prove positivity:
\[
\begin{array}{c|c|c|c|c}
\text{row}&R&U>&D<&
U-cD^2>\quad(c=1\text{ or }81/100)\\ \hline
1&7/10&3/2&11/10&29/100\\
1&41/50&109/60&6/5&113/300\\
2&7/10&7/5&5/4&43/320\\
2&41/50&5/3&7/5&593/7500 .
\end{array}
\tag{14}
\]
Each middle entry follows by direct substitution in (12).
For example at \(R=41/50\), the first \(U\) exceeds
\(3/4+2/3+2/5=109/60\), and the second exceeds
\(3/4+2/3+1/4=5/3\).
Concavity and (14) establish the assertions throughout the
whole radius interval.

Consequently (10) is positive through \(q=1/5\), and greater
than \(-\log(10/9)\) thereafter. Transporting back from \(q_0\)
costs less than
\[
                    \frac1{50}\log(10/9)<\frac1{450}.
\tag{15}
\]
Every main and real low profile therefore retains reserve
\[
                         \frac1{50}-\frac1{450}=\frac4{225}.
\tag{16}
\]

The real half derivative is
\[
\frac12\log(1+R^2+2R\cos2\pi q)
                   -\log(1+R^2-2R\cos2\pi q).
\tag{17}
\]
Its positivity reduces, at the smallest allowed cosine \(9/50\),
to \(U_h-D_h^2>0\), where
\[
U_h=1+R^2+9R/25,\qquad D_h=1+R^2-9R/25 .
\]
The difference is strictly concave by (13).
At \(R=7/10\), \(U_h>17/10,D_h<5/4\), leaving \(11/80\).
At \(R=41/50\), \(U_h>49/25,D_h<69/50\), leaving \(139/2500\).
Increasing the cosine only increases \(U_h-D_h^2\).
Thus the real half profile retains its full \(1/50\) reserve.

## 4. Last profile and the old upper band

The exact variation of the forced-weight rate
\(\nu_R(q)=-\Re g(q+ih_y)\) obeys
\[
                  \max_{0\le q\le q_0}
                       \{\nu_R(q)-\nu_R(q_0)\}<1/125 .
\tag{18}
\]
This is [bounded-prefix four, Section 4](research_mixed_next_lower_left_bounded_prefix_four.md),
whose proof applies on \(1/2\le R<1\).
It maximizes at \(\arccos(R/2)/(2\pi)\) and uses the tangent
to \(\log(2\sin\pi q)\) at \(1/6\).
No outgoing carrier varies along this comparison.
By (8), the last profile retains reserve
\[
                         \frac1{50}-\frac1{125}=\frac3{250}.
\tag{19}
\]

Put \(F(v)=E(1-v;y,z)\), \(S(v)=2\sin\pi v\), and
\(B(v)=|1-Ze^{2\pi iv}|\).
On \(q+1/5\le v\le1/2\), increase \(q,v\) together until
\(q=q_0\) or \(v=1/2\).
The exact multiplier of the allocated constant-prefix profile is
\[
\exp\frac d{dq}\{B_0+F(q+d)-\Re g(y)\}
                    =\frac{R S(v)^2}{D_q B(v)},\qquad d=v-q.
\tag{20}
\]
This retains the incoming chirp. It is equation (18) of the
earlier bounded-prefix theorem, independently of its radial restriction.

For \(q\le1/10\), one has \(R/D_q>70/37>3/2\),
\(S(v)^2>4/3\), and \(B(v)<2\).
The last two estimates are equations (20),(23) of
[the enlarged-band theorem](research_mixed_next_own_three_upper_band_old_face.md),
valid for the larger old outgoing-radius domain.
Thus (20) is greater than one.
For \(q\ge1/10\), \(v\ge3/10\), and the same theorem's
correlated outgoing inequality gives \(S(v)^2/B(v)>2\).
Since \(R/(1+R^2-9R/25)\) increases for \(R<1\),
\[
                         \frac{2R}{D_q}>\frac{700}{619}>1 .
\tag{21}
\]
Hence the entire band transport is increasing.
The \(q_0\) endpoint uses (8), and the \(v=1/2\) endpoint
uses (17). Every band profile retains reserve \(1/50\).
These are continuous rate comparisons; their endpoint need
not be a finite-grid index.

## 5. Every remaining positive upper row

The small-reflected-index theorem
[equation (6)](research_mixed_next_three_small_reflected_logarithmic_bound.md)
applies by \(R\le41/50,\rho>4/5\), and gives
\[
                         F(v)\le L_0-v/600
                                      \quad(0\le v\le1/5).
\tag{22}
\]
It is a rate inequality independent of a preceding factor.
The all-radius [upper-end lemma, Section 2](research_mixed_next_own_three_upper_end_last_reduction.md)
also gives \(F(v)\le L_0\)
when \(v\le q\).

If \(v\ge3/10\) but \(v<q+1/5\), the positive fixed-\(q\)
reflected force in
[the fixed-shared theorem, equations (6)--(11)](research_mixed_next_own_three_upper_band_fixed_shared.md)
moves this profile to the band boundary \(v=q+1/5\).
Its proof is likewise independent of the first factor.

For \(q\ge3/20\), \(q\le v\le3/10\),
[the shallower-strip theorem, Proposition 1](research_mixed_next_own_three_shallow_upper_strip_reduction.md)
gives
\[
                         F(v)\le\max\{L_0,F(3/10)\}.
\tag{23}
\]
It uses only the physical rate and the larger old outgoing
radius bound, so remains valid on (1).
The endpoint \(F(3/10)\) is covered by the band or the preceding
fixed-\(q\) comparison. Equations (19),(21) therefore pay (23)
with reserve at least \(3/250\).

It remains to consider \(q<3/20\), \(1/5<v<3/10\).
Increase \(q,v\) together until \(q=3/20\) or \(v=3/10\).
Throughout this path \(|u-v|\le1/4\).
The improved outgoing radius in (2) gives
\[
               B(v)^2<1+(8/7)^2=\frac{113}{49}
                                      <\left(\frac{31}{20}\right)^2,
\qquad S(v)^2>\frac{11}{8}.
\tag{24}
\]
For \(q\le1/10\), \(R/D_q>70/37\), so the multiplier
in (20) is greater than one even with these bounds.
For \(1/10\le q\le3/20\), use \(\cos2\pi q>7/12\) and
the increasing function \(R/(1+R^2-7R/6)\) to get
\[
\frac{R S(v)^2}{D_q B(v)}
 >
\frac{105}{101}\frac{11}{8}\frac{20}{31}
=\frac{23100}{25048}>\frac9{10}.
\tag{25}
\]
The last strict comparison is \(231000>225432\).
Only this final interval can cost rate. Its length is at most
\(1/20\), so its total cost is less than
\[
                       \frac1{20}\log(10/9)<\frac1{180}.
\tag{26}
\]
At either stopping endpoint (23) or the fixed-\(q\) comparison
applies, with reserve \(3/250\) or better.
Thus all profiles in this last strip retain reserve
\[
                       \frac3{250}-\frac1{180}
                                      =\frac{29}{4500}.
\tag{27}
\]
Together, (22), \(v\le q\), the fixed-\(q\) comparison, (23),
and (25) exhaust \(0\le v\le1/2\).
Every original upper physical rate, before any first factor is
attached, is therefore paid against the constant \(B_0\) with
reserve at least \(29/4500\).
All reflections keep \(L_0\), both radial terms, and integrable
outgoing logarithmic zeros.

## 6. Complete finite source and limitations

For the low next rows use the literal range
\(0\le j\le\lfloor3N/20\rfloor\), including its zero row.
The positive force and endpoint-uniform bounds in
[the low-physical theorem](research_mixed_next_lower_left_low_physical_blocks.md)
reduce this full positive group to the real low profile.
The uniform hypotheses in that result include the smaller
actual-height domain (1).

For the middle use
\[
\lfloor3N/20\rfloor+1\le j<\lceil N/2\rceil
\]
and the original canonical \(T_{0,N}\) from
[the complete-current theorem](research_mixed_next_lower_left_complete_currents.md).
Its half-grid cuts, horizontal alias heights \(-1/5,4\),
all four weighted vertical halves, both unweighted joins,
and the \(+N\) main measure are retained.
The theorem bounds each of these nine pieces by its main,
real-low or real-half profile.
It allows both signs of the next private height on the larger
interval \([-.108,.068]\), so (1) meets every height hypothesis.
The independent preceding factor is constant in this private
index, and may be attached to each estimate.

At \(q=0\), the original canonical reciprocal factorial is
continued by its exact inward-seam recurrence. The whole forced
Fourier polynomial instead uses its distinct absolute bound
\[
             |d_N(Y)|\le C_\tau N^{B_\tau}
                        e^{N\{-\Re g(y)+\tau\}}.
\tag{28}
\]
These are the two separate seam inputs in the current theorem;
no relative asymptotic for \(d_N\) is asserted.

For \(\lceil N/2\rceil\le j\le N-1\), the original zero-safe
numerator and endpoint-uniform factorial bounds give the physical
rates of Section 5 with arbitrary small uniform rate tolerance.
Their complete positive sum is bounded, including the last row,
both parities, and arbitrary positive subsets.
No division by a terminal row or a numerator value is used.

The main, low, half and last reserves are respectively at least
\(4/225,4/225,1/50,3/250\); the remaining upper rows have
reserve \(29/4500\).
Choose the total of the preceding-factor tolerance in (5),
the forced-weight tolerance, all finite-product and interpolation
tolerances, and half-grid continuity losses below \(1/1000\).
There are only finitely many source groups. Polynomial row
counts and the original \(N\) factors change only the polynomial
prefactor. The residual uniform rate gap is greater than
\[
                     \frac{29}{4500}-\frac1{1000}
                            =\frac{49}{9000}>\frac1{200}.
\tag{29}
\]
This proves (6) for the complete original sum. \(\square\)

A positive preceding sum may be used in (5) if its own complete
positive bound is available. A coherent preceding bound does
not give a positive bound for its individual terms.
Uniform fixed-length integrations preserve (6); derivatives
do not follow without corresponding source neighborhoods.

The original correction polynomial of rate \(77/50\), far-real
first contribution of rate \(153/100\), and already controlled
first groups of rate at most \(B_0\) satisfy (5) wherever their
own stated domains apply. The theorem supplies their complete
next-type-three attachments on the actual heights above.
It does not supply (5) for an unpaid first incoming main,
nor pay a remaining signed Fourier contour or establish
arbitrary short-word composition.
