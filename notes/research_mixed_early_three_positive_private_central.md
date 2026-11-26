# The early first 3,3 central sum at positive private height

Research deduction, 10 November 2026. The complete first cap can be
combined with the central part of its adjoining own-three factor
when that factor's private critical height is nonnegative. The
original early outgoing coordinates and all actual heights remain
fixed. This completes the central estimate for an initial \(3,3\)
pair, since nonpositive private heights were treated previously.
Its full high physical row tail remains separate.

The proof uses the sharper actual private height of a first
type-three cap. Its lower horizontal alias does not have that
sharper height and is instead bounded by the original main profile
using its full Fourier penalty. All ordinary aliases and upward
zero-mode joins remain in the finite source.

## 1. Original reference, source and statement

Fix an actual positive three/four open word of length at least three
beginning \(3,3\). Retain its coordinates
\[
 a_*=a_0+ic,\qquad b_*=b_0+id,\qquad
 s_*=s_0+ih_0,\qquad e_*=e_0+ih_e ,
\tag{1}
\]
where \(e_*\) is the first cap's private coordinate and \(s_*\)
the second vertex's private coordinate. Assume
\[
                    0\le h_0\le17/250.
\tag{2}
\]
The actual endpoint and ordinary-image statements give
\[
\begin{gathered}
 -9/125<c<21/1000,\quad
 -19/1000<h_e<37/1000,\quad .278<a_0<.391,\\
                         -.065<d<.068.
\end{gathered}
\tag{3}
\]
These bounds refer to the same original geometric solution.
No independently chosen point of their containing rectangles is
substituted for it.

Take unchanged-height targets
\[
 a=x+ic,\quad b=z+id,\qquad
 x\in[1/10,11/50],\quad z\in P=[11/50,9/20].
\tag{4}
\]
Let \(r_N=e^{-2\pi i/N}\), \(X=e^{-2\pi ia}\), \(Y=e^{-2\pi ib}\),
and retain
\[
\begin{gathered}
 R_{j,N}(a,b)=X^{-j}
 \frac{(r_NX;r_N)_j(r_NY;r_N)_j}{(r_N;r_N)_j^2},\\
 J_L=\lfloor3N/20\rfloor,\qquad J_R=\lceil N/2\rceil-1,\qquad
 C^{\rm mid}_{0,N}(X,Y)=\sum_{j=J_L+1}^{J_R}R_{j,N}(a,b).
\end{gathered}
\tag{5}
\]
The first cap is the literal complete polynomial \(U_{0,N}(w,X)\).
There are no type-four Fourier weights in this first pair.

The original phase allocation is
\[
\begin{split}
 \Xi_0(e,a)&=S(e)+J(e+a)-J(a)-i\pi ea,\\
 F_{00}(s;a,b)&=g(s+a)+g(s+b)-2g(s)+2\pi ias-g(a)-g(b).
\end{split}
\tag{6}
\]
The primitives, complete-end action \(S\), selected roots and
additive constants are precisely those of the
[joint low-/half-row theorem](research_mixed_early_joint_low_tail.md).
Set \(L_0=\operatorname{stat}_e\Xi_0\),
\(\phi_{00}=\operatorname{stat}_sF_{00}\), and
\(\kappa=1/2500000\). Define
\[
\begin{split}
 \Gamma(z)&=\Re L_0(a_*)+\Re\phi_{00}(a_*,b_*)\\
 &\quad+\Re\partial_b\phi_{00}(a_*,b_*)(z-b_0)
                                      -\kappa(z-b_0)^2,\\
 \gamma_*&=\kappa(a_0-11/50)^2>0.
\end{split}
\tag{7}
\]
The original first-coordinate marginals cancel:
\(L_0'(a_*)+\partial_a\phi_{00}(a_*,b_*)=0\).

**Theorem 1.** For every \(\tau>0\), both level parities satisfy
\[
 |U_{0,N}(w,X)C^{\rm mid}_{0,N}(X,Y)|
 \le C_\tau N^{A_\tau}
                 e^{N\{\Gamma(z)-\gamma_*+\tau\}}
\tag{8}
\]
uniformly on (4) and on a sufficiently small fixed ordinary-color
neighborhood of \(w=-2\). Every fixed derivative in that color
satisfies the same rate on a smaller neighborhood.
The exact finite rows, every cap row and every ordinary Fourier
correction are included.

## 2. Transport at positive private heights

Fix
\[
 s=v+i\eta,\quad 3/20\le v\le1/2,\quad 0\le\eta\le h_0,
 \qquad e=u+i\xi\in E_c=[.27,.49]+i[-.055,.04].
\tag{9}
\]
For the moment assume \(\xi\ge-.019\), and put
\(r=e^{2\pi c}\), \(R=e^{2\pi\xi}\), \(q=e^{-2\pi\eta}\).
The required elementary bounds are
\[
 3/5<r<23/20,\qquad R>7/8,\qquad 13/20<q\le1.
\tag{10}
\]
The upper bound on \(r\) is the unchanged early-cap bound.
For its lower bound use \(2\pi|c|<1/2<\log(5/3)\) when \(c<0\).
For \(R\), \(e^{-t}>1-t\) and
\((19/500)\pi<1/8\) suffice. For \(q\), the positive atanh
series gives
\[
 \log(20/13)>
 \frac{14}{33}+\frac{686}{107811}>
 \frac37>\frac{17\pi}{125}.
\tag{11}
\]
The last inequality follows from \(\pi<22/7\). These are written
rational witnesses, not evaluations of source enclosures.

Differentiation of (6), including the ordinary chirp, gives exactly
\[
 \partial_x\Re(\Xi_0+F_{00})
 =\log\frac{N_eN_s}{D^2},\qquad
 \begin{cases}
 N_e=|1-rR e^{-2\pi i(u+x)}|,\\
 N_s=|q-r e^{-2\pi i(v+x)}|,\\
 D=|1-r e^{-2\pi ix}|.
 \end{cases}
\tag{12}
\]
In particular \(q\) cannot be replaced by one when \(\eta>0\).

**Lemma 2.** The derivative (12) is positive on (4), (9)--(10).
If \(c\ge0\) and \(4/25\le x\le11/50\), it exceeds \(1/11\).

*Proof.* For \(x\le4/25\), the angular bounds give
\[
\begin{split}
 N_e^2&>1+\frac{49}{64}r^2+\frac78r=:A,\\
 N_s^2&\ge\frac{169}{400}+r^2=:C,\qquad
 D^2<1+r^2-r=:B .
\end{split}
\tag{13}
\]
Indeed \(u+x\in[.37,.65]\), while \(v+x\in[.25,.66]\).
The latter cosine is nonpositive, so the second squared modulus
increases with \(q\). Also
\[
 A-B=r(15/8-15r/64)>0,\qquad
 C-B=r-231/400>0
\]
by (10). Thus \(AC>B^2\).

For \(x\ge4/25\), the original rational angular witnesses in
the joint low-row proof give
\[
 \cos2\pi(u+x)<-6/25,\quad
 \cos2\pi(v+x)<-9/50,\quad \cos2\pi x>9/50 .
\]
Consequently
\[
\begin{split}
 N_e^2&>A_0=1+\frac{49}{64}r^2+\frac{21}{50}r,\\
 N_s^2&>C_0=r^2+\frac{117}{500}r+\frac{169}{400},\\
 D^2&<B_0=1+r^2-\frac9{25}r .
\end{split}
\tag{14}
\]
Direct multiplication gives coefficients of \(r^4,r^3,r^2,r,1\)
in \(A_0C_0-B_0^2\) equal to
\[
 -\frac{15}{64},\quad \frac{42213}{32000},\quad
 -1-\frac{81}{625}+\frac{8281}{25600}+\frac{2457}{25000},
 \quad\frac{22629}{20000},\quad-\frac{231}{400}.
\]
They imply the lower bound
\[
 A_0C_0-B_0^2>
 Q(r):=-\frac{15}{64}r^4+\frac{13}{10}r^3-\frac34r^2
                      +\frac{113}{100}r-\frac{231}{400}.
\tag{15}
\]
For the quadratic coefficient, one may use
\(8281/25600>8/25\), \(2457/25000>9/100\), and
\(1/4+81/625<2/5\). The other coefficient comparisons are direct.
Since \(r<23/20<6/5\) and \(r\ge3/5\),
\[
 Q'(r)>
 \frac{111}{40}r^2-\frac32r+\frac{113}{100}
 \ge\frac{33}{200}r+\frac{113}{100}>0.
\]
Its initial value is
\[
                         Q(3/5)=3237/40000>0.
\tag{16}
\]
This proves positivity on the second interval.

If \(c\ge0\), then \(r\ge1\),
\(Q(r)\ge Q(1)=1389/1600>4/5\), and
\(B_0\le3817/2000<2\). Thus
\[
 \frac{N_e^2N_s^2}{D^4}>
 \frac{A_0C_0}{B_0^2}>\frac65,\qquad
 \partial_x\Re(\Xi_0+F_{00})>
 \tfrac12\log(6/5)>\frac1{11}.
\tag{17}
\]
The last bound follows from the positive atanh series.
\(\square\)

## 3. The lower cap alias and the true cap ends

The actual first-three main height satisfies (3). Its main profile,
the real cuts, and the upper horizontal alias all satisfy
\(\xi\ge-.019\), hence Lemma 2 applies to them. The lower alias,
at \(\xi=-11/200\), requires a separate argument.

The original complete endpoint branch on \(E_c\) has
\[
 .17<\Re u_c(e)<.28,\qquad .01<\Re(e-u_c(e))<.32 .
\tag{18}
\]
The [cap phase source](research_mixed_first_cap_plateau_phase.md)
records these full-rectangle bounds with their original primitive.
The original complete-end phase is
\[
 F_{\rm end}(e,u)=-2J(1/2-u)-3J(u)-J(e-u)+i\pi eu .
\]
Since \(S(e)=F_{\rm end}(e,u_c(e))\) on its original critical branch,
\[
 \Xi_{0,e}(e,a)
 =-J'(e-u_c(e))+J'(e+a)+i\pi(u_c(e)-a).
\tag{19}
\]
Both sine arguments in (19) have real part strictly between zero
and one, including \(.37\le\Re(e+a)\le.71\).
Their original logarithms therefore have imaginary parts between
\(-\pi/2\) and \(\pi/2\), without an additional lift.
Together with \(x\ge.1\), (18) gives
\[
                         \Im\Xi_{0,e}<59\pi/50.
\tag{20}
\]
Integrate in the private height from \(-11/200\) to \(h_e\).
As \(h_e<37/1000\), the length is less than \(23/250\).
The whole lower alias retains its penalty \(11\pi/100\), so
\[
\begin{split}
 \Re\Xi_0(u-11i/200,a)-11\pi/100
 &<\Re\Xi_0(u+ih_e,a)
       +\frac{1357\pi}{12500}-\frac{1375\pi}{12500}\\
 &=\Re\Xi_0(u+ih_e,a)-\frac{9\pi}{6250}.
\end{split}
\tag{21}
\]
This is a comparison to the original main height, not a replacement
by an uncalibrated real-height cap profile. It is uniform in \(u\);
adding any ordinary phase preserves it.

The complete fixed-height cap theorem also retains a possible
physical right-row allowance \(\Delta_0<1/200\). It occurs only
when \(c>0\) and \(x<4/25\). Its underlying right-cut profile has
\(\xi=0\), and Lemma 2 saves more than
\[
             (11/50-4/25)/11=3/550>1/200
\tag{22}
\]
before transport reaches \(x=4/25\). The remaining transport is
favorable. Hence this finite-row allowance is paid with reserve.

Finally the true cap endpoints have rate
\[
              E_{\rm end}(c)=3/5+2\pi c_++(\log4)/100.
\]
Their joint derivative with \(F_{00}\) is separately
\[
                    \log(N_s/D).
\tag{23}
\]
If \(c\ge0\), it is positive. On the early subinterval this follows
from \(C-B=r-231/400>0\) in (13). On the later subinterval,
\[
 C_0-B_0=-231/400+297r/500\ge33/2000>0 .
\]
If \(c<0\), then \(r<1\), \(D\le2\), and
\(\cos2\pi(v+x)\le0\) throughout (9), so \(N_s>13/20\).
It follows that
\[
                    \log(N_s/D)>-\log(40/13)>-6/5.
\tag{24}
\]
For the last inequality the first four positive exponential terms
give \(e^{6/5}>401/125>40/13\).
Its entire unfavorable transport costs less than
\[
                         (3/25)(6/5)=18/125.
\tag{25}
\]
At \(x=11/50\), the original bare cap plane is greater than
\(79/100\). For \(c<0\) its true-end rate is below \(123/200\),
so the initial reserve is greater than \(7/40\). Subtracting (25)
leaves \(31/1000>0\). For \(c\ge0\) the transport is favorable,
and the old true-end comparison already applies. Thus every true
cap end is retained, independently of the regular-profile argument.

## 4. Calibration of the main ordinary line and upward joins

At \(x=11/50\), the completed cap-plane theorem controls every
main/cut/alias profile at its original actual reference. The
half-index contour theorem controls the whole ordinary main line
\([3/20,1/2]+ih_0\) with its unchanged supporting plane.
Adding them cancels the first marginal and retains both
first-coordinate quadratic losses:
\[
                         \Gamma(z)-2\gamma_*.
\tag{26}
\]
Lemma 2 transports each regular joint profile to (4); (21) disposes
of the lower cap alias by the actual main profile. The allowance
(22) and the true-end comparison (23)--(25) complete the cap
inventory. Hence (26) also controls the complete cap combined
with every point of the ordinary main line at early \(x\).

The zero-mode joins now run upward from zero to \(h_0\).
At \(x=11/50\), the old half-index Hessian is valid for
\[
 3/20\le\Re s\le1/2,\qquad -.108\le\Im s\le.068
\]
and the original plateau targets. Its negative real \(ss\)-entry
makes each vertical restriction of \(\Re F_{00}\) convex.
Thus either join is bounded by its real-cut or main-line endpoint.
The real cuts at \(3/20\) and \(1/2\) lie below the ordinary
plane by \(1/2000\). Lemma 2 and the same cap-end arguments
apply pointwise for every \(0\le\eta\le h_0\). They transport
the entire join, not only its endpoints, to early \(x\).
Consequently (26) pays both upward joins as well.
No early-domain Hessian or new moving critical point is assumed.

At the early targets themselves the joint low-/half-row theorem
bounds both real-cut rates, with the complete cap, by
\(\Gamma(z)-1/2000\). These will pay the ordinary vertical
Fourier corrections.

## 5. All original ordinary Fourier corrections

Write
\[
 Q_0(s;a,b)=g(s+a)+g(s+b)-2g(s)+2\pi ias .
\]
The difference \(Q_0-F_{00}\) is independent of \(s\).
Lemma 2 of the
[complete early central source](research_mixed_early_joint_central_source.md)
is an all-height argument estimate; its proof does not assume
the sign of the reference private height. It gives on the present
early real intervals
\[
 -11\pi/5<\Im Q_{0,s}<53\pi/50\quad(y\in\mathbb R),
 \qquad
 \Im Q_{0,s}>-77\pi/40\quad(y\ge0).
\tag{27}
\]
Its actual first-height requirement \(c>-.078\) follows from (3).

Use the same lower and upper ordinary index heights, \(-1/5\)
and \(4\). Since \(\partial_y\Re F_{00}=-\Im Q_{0,s}\),
the lower horizontal correction satisfies
\[
\begin{split}
 \Re F_{00}(v-i/5)-2\pi/5-\Re F_{00}(v+ih_0)
 &<\frac{53\pi}{50}\frac{67}{250}-\frac{2\pi}{5}\\
 &=-\frac{1449\pi}{12500}.
\end{split}
\tag{28}
\]
The positive private height in (2) has been retained in its
maximal length \(1/5+h_0\le67/250\).
For the upper horizontal,
\[
 \Re F_{00}(v+4i)-8\pi-\Re F_{00}(v+ih_0)
 <\frac{77\pi}{40}(4-h_0)-8\pi
 \le-\frac{3\pi}{10}.
\tag{29}
\]
Multiplying by any of the unchanged cap terms preserves these
comparisons.

At either real cut, (27) gives
\[
\begin{split}
 \partial_y(\Re F_{00}-2\pi y)&<-3\pi/40,
                                      &&y\ge0,\\
 \partial_y(\Re F_{00}+2\pi y)&>47\pi/50,
                                      &&y\le0.
\end{split}
\tag{30}
\]
Every upper or lower half-grid vertical Fourier correction is
therefore bounded by its own real-cut rate. These four sides
are jointly paid by the complete cap/real-cut bounds above.
No curvature estimate on the tall upper strip is used.

## 6. Completing the finite source and its ordinary-color scope

Use exactly the marked factorial interpolation and the cotangent
residue formula displayed in Section 6 of the complete early central
source. The two half-grid cuts enclose precisely the rows (5).
Every factorial argument on the ordinary rectangle
\([3/20,1/2]+i[-1/5,4]\), including its shifted arguments and
the outer ones, has real part in a fixed compact subset of \((0,1)\).
The exact factorial theorem is uniform on every fixed compact
imaginary-height interval. No new zero or pole is crossed.

The constant cotangent modes combine to \(+N\) times the original
real central integral. Move that integral to height \(h_0\),
retaining both upward endpoint integrals with their original signs.
Section 4 pays this line and both joins. The nonconstant modes
give exactly the two horizontal corrections and four vertical
half-sides paid in Section 5. All physical residues, scalar
coefficients, parity shifts and half-grid endpoint choices are
unchanged. Triangle inequalities are used only after this exact
finite decomposition.

The first cap is already summed completely by its fixed-height
source theorem. Sections 2--3 keep its main line, both cuts,
both aliases, all revived physical upper rows and both true index
ends. Combining these finite inventories leaves the gap
\(\gamma_*\) in (8), since \(2\gamma_*<1/2000\).
The finite contour lengths, half-grid shifts and symbol bounds
contribute polynomial factors and arbitrarily small rate tolerances.

The complete cap source holds for the whole real ordinary-color
interval. Discard its favorable angular loss in the regular
profiles and retain its uniform true-end bound. The same proof
therefore yields (8) for all real ordinary colors. The cap degree
is less than \(N\), whereas the ordinary factor is color-independent.
Interval Bernstein--Walsh continuation gives a fixed neighborhood
of \(-2\) with any prescribed additional rate tolerance, and Cauchy's
formula gives every fixed ordinary-color derivative on a smaller
neighborhood. This argument uses the polynomial product directly
and divides by no possibly zero factor. It proves Theorem 1.

Together with the nonpositive-height central theorem, (8) controls
the entire central block of every actual initial \(3,3\) pair at
the fixed early heights. The low block is already paid separately.
For the zero-drift class \(c\ge0,d\le0\), the all-angle high-row
theorem also pays its complete high block, so the full first pair
is bounded in that class regardless of the sign of \(h_0\).

Outside that class, this note makes no assertion about the complete
high physical row tail. It does not change an outer contour's
heights, estimate selected first Fourier monomials, provide a
whole-word or knot theorem, or prove short-partial-filling stability.

## Direct source versions

| Source | SHA-256 |
|---|---|
| research_mixed_early_joint_central_source.md | f19a7b5c42a4f372e9671c95dec5670f501065802fa96279b542efaa5005aec3 |
| research_mixed_early_joint_low_tail.md | 72ee3edebe390f213751e7774913d7d6552d6eff3bdea61b13f4d23159ad6606 |
| research_mixed_cap_early_fixed_height_full_source.md | d930407eaa5a0bb7c735ee9521c6d352f637124c57c5593cbb1813f069f7d423 |
| research_mixed_first_cap_plateau_phase.md | 159a1b89eebcb72fa9ac3395435086f066b3e648c389e2417e0b61fb490ff612 |
| research_mixed_first_cap_plateau_completion.md | 4b1a55000a114835ce4b2868b79f4bec63ee781d6d997f7fa6b37f7896e4e87d |
| research_mixed_half_index_contour.md | ed8d13779e734803090f778d01ddc334469cbfb7a35154ba48d6eb462c28c57e |
| research_mixed_open_word_endpoint_rectangles.md | ac5603badc00d42e98d17a1c5948cae011a6abd991d5249fa61d4224a829ad07 |
| research_mixed_all_angle_high_row_sign_class.md | 3a959f0a6bb064767e753e90061a2d9ef323268e79cbdf19c1043a6fe9691144 |
| exact_factorial_interpolation_and_complex_contours.md | 1f34f65437dfe0bfb4062a7a74840beae1676353cf13bb8a86f8849a8a36bc72 |
| research_complete_boundary_full_index_interval.md | 450cd41db9c49049e9b80a41c83828a2f0fafa43f986803bc57b93be580a57ef |

All directly used source statements and proof portions were read.
The proof uses written inequalities only. No mathematical numerical
evaluation, saved-value arithmetic, import, compilation, test, or
frozen-source edit was performed.

