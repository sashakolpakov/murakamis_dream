# Complete first left connections over the early second interval

Private written deduction, 11 November 2026. For an actual word
beginning with \(444\), the first coordinate can follow either of
its original left paths while the second target lies in
\([1/10,11/50]\) at its actual negative height. The new pieces are
the entire real interval from zero to one tenth and the unselected
negative-height join there. The complete cap, both complete
conditional kernels, and every original Fourier factor are retained.

The real estimate uses a new low-row ratio on the smaller outgoing
angular interval. The negative join uses a common convex envelope
of the actual finite currents, calibrated separately at its two
endpoints. Neither argument uses convexity of a finite modulus.

## 1. Exact source and result

Fix the same actual positive three/four word of length \(m\ge4\)
beginning with \(444\) as in
[the unselected early horizontal](research_mixed_complete44_second_early_unselected_first_horizontal.md).
Keep its coupled reference \(r_j=a_j+ic_j\), logarithmic lifts,
ordinary color, and attached following leg. Put
\[
 E=[1/10,11/50],\qquad P=[11/50,9/20],\qquad
 y=q+ic_2,\quad q\in E,\qquad z=u+ic_3,\quad u\in P .
 \tag{1}
\]
In particular
\[
 -.078<c_1<-.020,\quad -.102<c_2<-.001,\quad
 -.108<c_3,h_s,h_t<-.001,\quad -.051<h_e<-.019 .
 \tag{2}
\]
These are containing bounds for the actual reference, not
independently variable reference data. At \(m=4\), the third
vertex is ordinary with its original attached following leg.

For \(r_N=e^{-2\pi i/N}\), retain
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
Here \(d_N\) is the original polynomial of degree less than \(N\)
with \(d_N(r_N^j)=1/P_j\); its endpoint forcing is retained.
The literal density, for either first Fourier choice, is
\[
 \mathscr K_{\sigma,N}(w;a,y,z)
 =U_{1,N}(w,X)d_N(X)X^{-\sigma N}C_{1,N}(X,Y)
                          d_N(Y)C_{1,N}(Y,Z),\qquad \sigma=0,1 .
 \tag{4}
\]
The second coordinate is unselected. Carry the outgoing multiplier
\(|d_N(Z)|^{1/2}\) without division, including at its zeros.

Use the original bare phases
\[
\begin{split}
 \Psi(e,a)&=S(e)+g(e+a)-g(a)-g(e)-\frac{i\pi}{2}(e-e^2),\\
 Q(s;b,c)&=g(s+b)+g(s+c)-3g(s)-g(b)-g(c)+2\pi ibs .
\end{split}
 \tag{5}
\]
Here \(g=J+i\pi(v-v^2)/2\), \(J'=\Log(2\sin\pi v)\), with
the original absolute constants and branches. Thus
\(\Xi=\Psi-g(a)/2\), \(F_2=Q(s;a,y)-g(a)/2-g(y)/2\),
and \(F_3=Q(t;y,z)-g(y)/2-g(z)/2\).
The action throughout this note is exactly
\[
 \Lambda_{123}(z)=
 \Re\{L_1(r_1)+\phi_2(r_1,r_2)+\phi_3(r_2,r_3)
                   +\partial_2\phi_3(r_2,r_3)(z-r_3)\}.
 \tag{6}
\]
Here \(L_1,\phi_2,\phi_3\) are the same stationary actions of
\(\Xi,F_2,F_3\) as in the cited horizontal source.

Define the two oriented paths
\[
\begin{split}
 \Gamma_0&:[0,1/10]\ \cup\
     [1/10,\,1/10+ic_1]\ \cup\
     ([1/10,9/20]+ic_1),\\
 \Gamma_1&:[0,1/10]\ \cup\
     [1/10,\,1/10+i/100]\ \cup\
     ([1/10,9/20]+i/100).
\end{split}
 \tag{7}
\]
Their segments have the indicated successive orientations.

**Theorem 1.** Uniformly in (1), both level parities and a
sufficiently small fixed ordinary-color disk about \(-2\),
\[
 |\mathscr K_{\sigma,N}(w;a,y,z)|\,|d_N(Z)|^{1/2}
 \le C N^B e^{N\{\Lambda_{123}(z)-10^{-13}\}},
                         \qquad a\in\Gamma_\sigma .
 \tag{8}
\]
The same rate, with a polynomial factor, bounds the oriented
integral over either path with its original density \(N\,da\).
Fixed ordinary-color derivatives obey a smaller positive gap
on a smaller disk.

The proof below gives the more explicit new bounds
\[
\begin{array}{ll}
 a=x,\quad 0\le x\le1/10,\quad \sigma=0,1:
       &\Lambda_{123}(z)-1/4000,\\
 a=1/10+ih,\quad c_1\le h\le0,\quad \sigma=0:
       &\Lambda_{123}(z)-10^{-12}.
\end{array}
 \tag{9}
\]
No right first connection, whole first coefficient, full
\(R_{44,N}\), or whole second period is asserted.

## 2. One common raw envelope and its endpoint calibrations

We first specify the profiles being compared. For \(a=1/10+ih\),
\(c_1\le h\le0\), let \(A(h)\) be the maximum of
\[
\begin{split}
 &\max_{.27\le e_R\le.49}\Re\Psi(e_R+ih_e,a),\
       \Re\Psi(.27,a),\ \Re\Psi(.49,a),\\
 &\max_{e_R}\Re\Psi(e_R-.055i,a)-.11\pi,\qquad
       \max_{e_R}\Re\Psi(e_R+.04i,a)-.08\pi,\\
 &E_*=\frac35+\frac{\log4}{100}.
\end{split}
 \tag{10}
\]
The [independent-height cap source](research_mixed_cap_early_fixed_height_full_source.md)
proves this complete envelope: all cap rows, private joins,
horizontal aliases and vertical halves are included. Its own-four
upper-row allowance is zero. Its general true-end rate is
\(E_*+2\pi h_+\), so (10) is precisely its rate for the
present nonpositive heights.

Retain the full ordinary private collection \(\mathscr C_4\):

| Piece | Private point \(s\) | Penalty \(\omega\) |
|---|---|---|
| Main | \(v+ih_s,\quad 1/8\le v\le1/2\) | \(0\) |
| Both unweighted joins | \(\ell+i\eta,\quad \ell=1/8,1/2,\ h_s\le\eta\le0\) | \(0\) |
| Lower horizontal alias | \(v-i/5\) | \(2\pi/5\) |
| Upper horizontal alias | \(v+4i\) | \(8\pi\) |
| Four weighted vertical halves | \(\ell+i\eta,\quad \eta\in[-1/5,0]\cup[0,4]\) | \(2\pi|\eta|\) |

For physical rows put
\[
 E_1(t;a,y)=I_a(t)+I_y(t)-3J(t)-2\pi ht,\qquad
 I_b(t)=\int_0^t\log|1-e^{-2\pi i(b+v)}|\,dv .
 \tag{11}
\]
Define
\[
 B(h;y)=\max\left\{
   \sup_{(s,\omega)\in\mathscr C_4}(\Re Q(s;a,y)-\omega),\
   \sup_{1/2\le t\le9/10}E_1(t;a,y),\ -2\pi h\right\}.
 \tag{12}
\]
The third conditional factor is independent of \(a\).
Its complete reduction in the unselected early horizontal,
equation (10), gives the bare envelope
\[
 D_3(y,z)=\max\left\{
  \max_{1/8\le t_R\le1/2}\Re Q(t_R+ih_t;y,z),\
  \Re Q(1/8;y,z),\ \Re Q(1/2;y,z),\ -2\pi c_2\right\}.
 \tag{13}
\]
This retains all its low/high rows and all its central currents.
In particular it is not just a chosen local saddle profile.

The complete allocated same-source envelope is
\[
 \mathcal E(h;y,z)=A(h)+B(h;y)+W_0(h)
                     -\Re g(y)+D_3(y,z)-\tfrac12\Re g(z),
 \qquad W_0(h)=\max\{-\Re g(1/10+ih),0\}.
 \tag{14}
\]
Both upper alternatives of the original first Fourier polynomial
are present. On this negative-height interval, its factorial
alternative dominates because the radial primitive is nonpositive
on real angles between zero and one half. The full second and
outgoing weights have the indicated original negative-height upper
rates. Formula (14) adds the two internal incidences exactly; no
finite square root or Fourier value has been divided out.

The two raw endpoint comparisons needed below are
\[
 \mathcal E(c_1;y,z)\le\Lambda_{123}(z)-10^{-10},
 \qquad
 \mathcal E(0;y,z)\le\Lambda_{123}(z)-1/2000.
 \tag{15}
\]
For the first, use the proof of the unselected early horizontal,
Sections 2--6. Its main/cut/last anchors and transports pay every
cap alternative with every first ordinary current, both first
physical blocks, and each third profile (13), with common raw
reserve \(10^{-10}\). In particular its first high-row argument
pays every continuous high rate before finite summation. Its
alias contours are exactly the height-four collection above.
The literal last carrier is \(-2\pi c_1\), as in (12).

For the second, use Sections 2--3 of
[the selected early-second left join](research_mixed_complete44_first_selected_early_second_left_join.md)
at \(h=0\). That proof first pays every cap/core pair at the old
second face, then transports each pair through \(E\) while retaining
each third controlling profile. Its first aliases have height four;
both unweighted joins reduce to their main and real endpoints.
Its zero-drift high theorem pays every high physical rate by the
half profile. Thus it pays the whole collection (10)--(14),
not just a signed product. At height zero the selected monomial
has modulus one and its two Fourier upper alternatives coincide
with \(W_0(0)\). The true-end rate is exactly \(E_*\).
This proves the second inequality of (15).

Both uses of (15) are raw profile implications of the cited proofs.
An upper bound for a finite cancelling sum is not used as a lower
bound or as a bound on its separate profiles.

## 3. The full negative-height join

We verify that the common envelope remains a valid full source
and is convex when the outgoing real coordinate is in \(E\).
This is the source construction of
[the negative first-height face](research_mixed_first_four_four_negative_height_face.md),
with its old endpoint calibrations replaced by (15).

Split the first conditional sum into
\[
 0\le j\le\lfloor N/8\rfloor,\quad
 \lfloor N/8\rfloor+1\le j\le\lceil N/2\rceil-1,\quad
 \lceil N/2\rceil\le j<N .
 \tag{16}
\]
The [exact attached low-row theorem](research_mixed_first_attached_low_row_transport.md)
explicitly covers \(x=1/10,\ q\in E,\ c_1\le h\le0\) and
the actual second height. Its force exceeds \(e^{1/200}\)
through index \(1/5\). Stopping at \(1/8\) bounds the first
block by 201 times its last row, whose rate is the real cut
already in (12).

For the middle block retain the original marked factorial
interpolant
\[
 e^{2\pi iNas}\Pi_N(a+s)\Pi_N(y+s)
                         E_N(a)E_N(y)E_N(s)^3 .
 \tag{17}
\]
In (17), \(\Pi_N(v)=\widehat P_N(Nv)\) and
\(E_N(v)=1/\Pi_N(v)\), where the negative-root marking is
\[
 \widehat P_N(u)=G_N(u)
       \exp\{\pi iu/2-\pi iu(u+1)/(2N)\}.
\]
This is exactly equation (3) of the Fourier-weight source and
agrees with \(P_j\) at every physical index.
The half-grid cuts tend to \(1/8,1/2\).
At the changed outgoing angles its shifted real parts satisfy
\[
 \Re(s+a)\in[.225,.6],\qquad \Re(s+y)\in[.225,.72].
 \tag{18}
\]
They remain in compact subsets of the original regular factorial
strip at every fixed height from \(-1/5\) to \(4\).
The exact residue formula gives its positive \(N\) zero-mode
density, both horizontal aliases and all four weighted vertical
halves. Moving only the zero mode to \(h_s\) retains both
unweighted joins. Every resulting term is in \(\mathscr C_4\).

Every physical high rate up to \(9/10\) is retained in (12).
For \(t=1-v\ge9/10\), the reflection argument used in the
negative-face source requires only \(v\le x,q\le1/2\).
Here \(x=1/10\), \(q\ge1/10\), so its exact inequality gives
\[
 E_1(1-v;a,y)-E_1(1;a,y)
       \le J(v)-(-2\pi h)v\le0,\qquad E_1(1;a,y)=-2\pi h .
 \tag{19}
\]
The zero-safe integrated product bounds retain every finite index,
including \(N-1\) and both parity stops, without dividing by a
half or last row. Equations (10)--(14), the complete third
reduction, and the whole Fourier upper bounds therefore bound
the full density by a polynomial times
\(\exp N(\mathcal E(h;y,z)+\tau)\), for any fixed \(\tau>0\).

For convexity put \(C_a(h)=\Re\cot\pi(1/10+ih)\).
The negative-face proof gives, on the full actual interval,
\[
 C_a(h)>245/144>3/2,\qquad
 \Re\cot\pi(t+i\eta)\le3/2
                  \quad(1/5\le t<1,\ \eta\in\mathbb R).
 \tag{20}
\]
Its written witnesses use \(2\pi|h|<1/2\),
\(\cosh(2\pi h)<8/7\), and the pentagon inequalities
\(\sin(\pi/5)>7/12,\ \cos(\pi/5)>4/5\).
Every fixed cap or middle point thus satisfies
\[
\begin{split}
 \partial_h^2\Re\Psi(e,a)
     &=\pi\{C_a(h)-\Re\cot\pi(e+a)\}>0,\\
 \partial_h^2\Re Q(s;a,y)
     &=\pi\{C_a(h)-\Re\cot\pi(s+a)\}>0 .
\end{split}
 \tag{21}
\]
The outgoing target does not enter either difference.
The chirps are affine in \(h\); all sampling penalties are fixed.
For \(1/2\le t<9/10\),
\[
 \partial_h^2 E_1(t;a,y)
     =\pi\{C_a(h)-\Re\cot\pi(a+t)\}>0 ,
 \tag{22}
\]
because \(3/5\le\Re(a+t)<1\). The outgoing numerator,
including any wrap, is independent of \(h\).
At \(t=9/10\) the continuous integrated rate is a pointwise
limit of convex functions, also at \(h=0\).
The carrier \(-2\pi h\) is affine, the cap true-end ceiling is
constant, and \(-\Re g(a)\) is convex. Maxima, suprema and
sums preserve convexity. Thus \(\mathcal E(h;y,z)\) is convex.

The endpoint bounds (15) now give
\[
 \mathcal E(h;y,z)\le\Lambda_{123}(z)-10^{-10}
                              \qquad(c_1\le h\le0).
 \tag{23}
\]
Choose the finitely many source and color allowances inside
this reserve. This proves the second line of (9).
The literal differential on the join is \(da=i\,dh\);
its fixed length and the original density \(N\,da\) cost
only a polynomial factor.

## 4. The common real first interval away from zero

Let \(0<\rho<1/10\) be fixed, and let \(\rho\le x\le1/10\)
with \(a=x\). Both first monomials in (4) have modulus one.
The complete cap construction in Sections 2 and 4 of
[the real first-interval proof](research_mixed_four_four_real_first_interval.md)
is independent of the following target. It therefore applies
unchanged to the present \(q\in E\). We recall the parts that
prevent an endpoint loss from being hidden.

Its compact low cap rows increase to \(.27\), and its compact
upper rows decrease to \(.49\). The central source keeps the
five private profiles of (10), now evaluated at \(a=x\).
The private curvature inequality
\[
 -\Re\Psi_{ee}>2\pi\Re\cot\pi e-\pi\Re\cot\pi(e+x)>0
 \tag{24}
\]
holds on the same cap rectangle for every \(\rho\le x\le1/10\).
Thus all cap joins and vertical aliases are still controlled by
those five profiles. For the true upper cap end, with
\(i/N=1-\delta\), the minimum-arc inequality gives
\[
 I_x(1-\delta)-J(1-\delta)
    \le J(\delta)-2J(\delta/2)\le\delta\log2 .
 \tag{25}
\]
Combined with its all-real endpoint coefficient rate
\(3/5+\delta\log2\), this is the same \(E_*\) as in (10)
for \(\delta\le1/100\). The lower true-end rate is smaller.
The proof clips numerator logarithms before passing to integrals,
so (25) includes an omitted arc containing a zero. No vanishing
numerator is used as a denominator. The cap source hence retains
the full original rows and both true ends at every fixed \(\rho\).

The ordinary low-ratio proof in that older real-interval note
used \(q\ge.22\); it is not invoked on the new interval.
Here is the needed exact replacement. Write
\[
 S(t)=2\sin\pi t,\qquad R=e^{2\pi c_2}\in(0,1).
\]
For \(t=(j+1)/N\le1/8\), the exact own-four row recurrence at
real \(a=x\) is
\[
 \frac{|R_{j+1,N}(x,y)|}{|R_{j,N}(x,y)|}
  =\frac{2\sin\pi(x+t)\,
             |1-R e^{-2\pi i(q+t)}|}{S(t)^3}.
 \tag{26}
\]
Here \(0\le x\le1/10\) is allowed. Its first numerator is at
least \(S(t)\), since \(x+t\le.225<1/2\).
Radial minimization gives
\[
 |1-R e^{-2\pi i(q+t)}|\ge
 \begin{cases}
  \sin(2\pi(q+t)),&q+t\le1/4,\\
  1,&1/4\le q+t\le.345 .
 \end{cases}
 \tag{27}
\]
If \(t\le1/10\), this modulus is greater than \(1/2\),
whereas \(S(t)^2\le(3-\sqrt5)/2<2/5\).
Here the smallest relevant sine is \(\sin(\pi/5)>7/12\).
If \(1/10\le t\le1/8\), it is greater than \(9/10\), whereas
\(S(t)^2\le2-\sqrt2<16/25\).
The sine comparison follows from
\(\sin(2\pi/5)=\cos(\pi/10)>9/10\);
the latter follows already from
\(\cos(\pi/10)\ge1-\pi^2/200>19/20\).
The denominator comparisons follow from
\(\sqrt5>11/5\) and \(\sqrt2>34/25\).
Consequently
\[
 \frac{|R_{j+1,N}|}{|R_{j,N}|}>5/4
                 \qquad(0<(j+1)/N\le1/8).
 \tag{28}
\]
All numerator factors in this range are nonzero. The entire
positive low block is therefore less than five times its last
row. Its limiting rate is the real cut \(s=1/8\).
This is an exact finite recurrence, including \(x=0\) and \(j=0\).

For \(x\ge\rho\), the
[all-angle zero-drift theorem](research_mixed_all_angle_high_row_sign_class.md)
applies with first height zero and second height negative.
It bounds all rows from \(\lceil N/2\rceil\) through \(N-1\)
by the continuous half-row rate, at both parities. No literal
half-row value is divided out.

The middle source uses exactly \(\mathscr C_4\), now at \(a=x\).
The real shifted arguments lie in
\([1/8+\rho,.6]\) and \([.225,.72]\).
Thus the exact fixed-height factorial interpolation remains
regular through upper height four. This replaces the height-two
rectangle printed in the older real-interval proof.
No estimate at the smaller \(x\) is presumed for its joins or
aliases: all of them remain in the raw collection.

For fixed retained cap and ordinary points put
\[
 D=2\sin\pi x,\quad
 N_e=|1-e^{-2\pi i(e+x)}|,\quad
 N_s=|e^{-2\pi\Im s}-e^{-2\pi i(\Re s+x)}|.
 \tag{29}
\]
The exact derivative, including the ordinary chirp and the
whole first Fourier rate, is
\[
 \partial_x\{\Re\Psi(e,x)+\Re Q(s;x,y)-J(x)\}
                      =\log\frac{N_eN_s}{D^3}>\frac13 .
 \tag{30}
\]
Indeed \(.27<\Re e+x\le.59\) makes \(N_e>1\), while
\(1/8<\Re s+x\le.6\) makes \(N_s\ge1/\sqrt2>7/10\)
by radial minimization. Also \(D<5/8\).
Thus the logarithm exceeds \(\log2>1/3\).
For a true cap end the derivative is
\[
 \partial_x\{E_*+\Re Q(s;x,y)-J(x)\}
                 =\log\frac{N_s}{D^2}>\log(3/2)>\frac13 .
 \tag{31}
\]
All penalties and every third profile are independent of \(x\).
The complete real first Fourier rate is
\(\max\{-J(x),0\}=-J(x)\), including its forcing.

Apply (30)--(31) to every profile before taking a maximum.
The low and high reductions above leave only real cuts already
in \(\mathscr C_4\). At \(x=1/10\), the second comparison of
(15) pays this exact height-four collection and every third
profile. Thus, for each fixed \(\rho>0\) and \(\tau>0\),
\[
 |\mathscr K_{\sigma,N}(w;x,y,z)|\,|d_N(Z)|^{1/2}
 \le C_{\rho,\tau}N^{B_{\rho,\tau}}
 \exp N\left\{\Lambda_{123}(z)-\frac1{2000}
                        -\frac{1/10-x}{3}+\tau\right\},
 \quad \rho\le x\le1/10 .
 \tag{32}
\]
This proves the complete real source away from zero. It includes
all original finite indices, both unweighted joins and both
sampling aliases with their four weighted sides. Uniform errors
and half-grid displacements are absorbed in \(\tau\).

## 5. Zero endpoint and connected paths

The exact Laurent support in \(X\) of the first part of (4) is
\[
 [-(1+\sigma)N+1,\ (2-\sigma)N-2].
 \tag{33}
\]
Indeed the cap and \(d_N(X)\) each have degrees between zero
and \(N-1\), while each conditional term has degrees in
\([-j,0]\). The remaining factors and the outgoing modulus
multiplier are constant in \(X\); they do not enlarge this
band, even if the multiplier vanishes.

Use Lemma 1 of
[the exact real endpoint-continuation proof](research_mixed_four_four_real_first_endpoint.md).
For each chosen rate cost \(\varepsilon>0\), it first fixes a
Chebyshev ellipse parameter, then a small interval length
\(b>0\), then \(0<\rho\ll b\), all before \(N\). Every Laurent
polynomial with frequencies in \([-2N,2N]\), bounded on
\([\rho,b]\), extends to \([0,b]\) at cost at most
\(2(4N+1)e^{\varepsilon N}\).
Its proof clears only the explicit tangent-substitution
denominator, which is nonzero on the chosen ellipse.
It does not divide by any source factor or continue a factorial
symbol through zero.

Apply that lemma to the whole expression (4) times
\(|d_N(Z)|^{1/2}\), whose band is (33). Choose, for example,
\(\varepsilon=1/16000\), fix \(b,\rho\), and then choose all
source and color allowances in (32) below \(1/16000\).
The resulting loss is less than \(1/8000\), so the gap
\(1/4000\) stated in (9) holds on \([0,b]\) and also on
\([b,1/10]\) by (32). No constants are required to stay uniform
as \(\rho\) tends to zero. The outgoing weight and both first
Fourier choices are uniform throughout this fixed construction.

The cap source gives a fixed ordinary-color disk after the
allowance is chosen. All continuation estimates are applied
uniformly on a smaller such disk; Cauchy's formula gives fixed
color derivatives. Alternatively the same real-color coefficient
bounds and degree less than \(N\) permit the real-color
continuation in the endpoint source. No modulus halfweight is
differentiated.

We now concatenate only already controlled pieces:

* Both paths start with the new real interval in (9).
* The negative join is the second estimate in (9).
  The unselected horizontal from \(.1+ic_1\) to \(.22+ic_1\)
  is the complete early horizontal, with gap \(10^{-12}\).
  Its continuation to \(.45+ic_1\) is Theorem 1, equation (8),
  of [the central first-plateau theorem](research_mixed_complete44_second_early_central_four.md),
  with gap \(10^{-11}\).
* The selected positive join is the selected early-second
  left-join theorem, and its whole horizontal to
  \(.45+i/100\) is
  [the selected early-second horizontal](research_mixed_complete44_first_selected_early_second_horizontal.md).
  Each retains a fixed gap \(1/4000\) after allowance.

The original action (6), the two full internal Fourier weights,
and the outgoing halfweight agree on every piece. A finite
intersection of the ordinary-color disks, followed by a smaller
allowance, gives (8). Fixed path lengths and the single density
\(N\,da\) change only the polynomial factor. Orientations remain
those of (7); reversing the negative join in a contour identity
changes its sign, not this modulus estimate.

The paths stop at their right plateau endpoints. No equality
with a whole first-period integral has been used. The remaining
right first connections and real arcs, the full coherent
\(R_{44,N}\), and a complete second-period theorem remain
separate obligations. The result is restricted to actual initial
\(444\), early second targets at their original negative height,
and an actual third unselected plateau. It asserts no new
initial-\(443\), whole-word, or filling conclusion.

## Direct source versions

| Source | SHA-256 |
|---|---|
| research_mixed_complete44_second_early_unselected_first_horizontal.md | 90ea9fe2c40c0dd53bdcc9da10e0c5d407f9a003d4bd0ae15e929db9e28d3dee |
| research_mixed_complete44_first_selected_early_second_left_join.md | f478fee11cbc10d470857c1127765438a4e3bc307b671114197e37987d10ead4 |
| research_mixed_complete44_first_selected_early_second_horizontal.md | cb1bcdee71d415eb9edd250666b39b0b5826386c414fdca80dc1c9630ebc2985 |
| research_mixed_complete44_second_early_central_four.md | e5be8082613eac6887d3aca857703e4ac5b511c430f35ca91fa388c71a924f45 |
| research_mixed_first_four_four_negative_height_face.md | f50598305505a5dde4537fc15d6ed114b8e3a01eb87d69cff5ac36e0829b40a3 |
| research_mixed_four_four_real_first_interval.md | b848eb005f99d57259662ef3a864b207e093b6ebfaf4c34c2dbcc1e9727d58fc |
| research_mixed_four_four_real_first_endpoint.md | 4ceec7f835d08ef971b3b3ccadcf7eecd74e48db3d422cbd09e5611c0572c122 |
| research_mixed_cap_early_fixed_height_full_source.md | d930407eaa5a0bb7c735ee9521c6d352f637124c57c5593cbb1813f069f7d423 |
| research_mixed_first_attached_low_row_transport.md | 8ef728d3808e1480d85a81c1ed8f7eebda99392d0b11f1262e4a47b5a2b196d3 |
| research_mixed_all_angle_high_row_sign_class.md | 3a959f0a6bb064767e753e90061a2d9ef323268e79cbdf19c1043a6fe9691144 |
| research_mixed_fourier_weight_continuation.md | 0bae41d83f414eb91fd137de1242120a11408147d56ec752e466ca5ed7e7f48e |
| exact_factorial_interpolation_and_complex_contours.md | 1f34f65437dfe0bfb4062a7a74840beae1676353cf13bb8a86f8849a8a36bc72 |

Author full proof readback, all twelve directly used source
implication reads, and all twelve source-hash checks are complete.
Independent full proof/direct-source review is required before adoption.
No mathematical numerical evaluation, saved-value arithmetic,
test, import, compilation or frozen-source edit is used.
