# A log-two decrease for the complete cap on the whole real arc

Research deduction, 8 November 2026. A quantitative gap at the
half-face departure strengthens the complete real-arc cap bound.
The actual critical-action branch decreases at speed at least
\(\log2\); the fixed-departure branch stays strictly below the
same affine upper envelope. Thus the whole original finite cap
has this stronger upper rate throughout \(1/2\le a\le7/10\).

The proof uses the existing complete contour and its full source
inventory. It does not assert a nonzero asymptotic expansion on
the whole arc, or dominance of the actual saddle over the
departure. No numerical evaluation or frozen-source edit is used.

## 1. The original complete envelope

Retain the exact original cap and phases of
[the complete departure envelope](research_mixed_cap_uniform_departure_envelope.md):
\[
\begin{gathered}
 U_{0,N}(w,e^{-2\pi ia})
  =\sum_{j=0}^{N-1}H_N(w,r^{-j})p_j(e^{-2\pi ia})/P_j,\\
 M(a)=\Re\mathcal T(a,-2),\qquad
 R_d(a)=\Re\Psi(e_d,a,-2),\qquad
 \mathcal E(a)=\max\{M(a),R_d(a)\}.
\end{gathered}
\tag{1}
\]
The ordinary color is \(w\). The private departure is fixed:
\[
 p_d=\frac{23}{144}+\frac{11\sqrt2}{12}i,\qquad
 e_d=\frac{\Log p_d}{2\pi i}=E_d-i\eta_d,\qquad
 K=|p_d|^2=\frac{35377}{20736}.
 \tag{2}
\]
In particular \(23/100<E_d<6/25\).
The original action is
\[
 \Psi(e,a,-2)=S(e)+J(e+a)-J(a)-i\pi ae.
 \tag{3}
\]
All primitive constants, branches, carriers and finite scalars
are unchanged.

The complete envelope theorem, including every physical row,
all six weighted currents and every unweighted main-path join,
proves
\[
 |U_{0,N}(-2,e^{-2\pi ia})|
 \le C_\tau N^{B_\tau}e^{N(\mathcal E(a)+\tau)}
 \qquad(1/2\le a\le7/10)
 \tag{4}
\]
for every \(\tau>0\), with both level parities.
It also retains
\[
 M(a)\le M_{\mathrm{half}}-\log2\,(a-1/2),
                  \qquad M_{\mathrm{half}}=M(1/2).
 \tag{5}
\]
This follows from the exact original critical multiplier
\(|\exp\mathcal T_a|<1/2\), not from a ratio of signed finite sums.

## 2. A quantitative half-face departure gap

Let \(e_+\) be the actual half-face critical point. The
[complete half-cap theorem](research_mixed_half_face_complete_cap_packet.md)
and [its action refinement](research_mixed_half_face_cap_action_upper.md)
give
\[
 \frac{17}{50}<\Re e_+<\frac7{20},\qquad
             \frac3{64}<-\Im e_+<\frac1{20}.
 \tag{6}
\]
The fixed departure has the stronger depth bounds
\[
                      \frac1{25}<\eta_d<\frac1{20}.
 \tag{7}
\]
For the lower bound, \(K>5/3\) and
\[
 \log(5/3)>
 2\left(\frac14+\frac1{3\cdot64}\right)
       =\frac{49}{96}>
       \frac{88}{175}>\frac{4\pi}{25}.
 \tag{8}
\]
As \(\eta_d=\log K/(4\pi)\), this proves the first inequality.
For the second, \(K<7/4<e^{\pi/5}\); the positive exponential
series at \(\pi/5>5/8\) already gives this bound.
Thus both private heights in the joining segment belong to
\((-1/20,-1/25)\).

The straight displacement from \(e_+\) to \(e_d\) consequently has
\[
 |\Delta E|>1/10,\qquad |\Delta h|<1/100,\qquad
                   \frac{|\Delta h|}{|\Delta E|}<1/10.
 \tag{9}
\]
On its whole containing rectangle the original half-face Hessian is
\[
 -\Psi_{ee}(e,1/2,-2)
  =\frac{2\pi}{\sin(2\pi e)}
   +\frac{2\pi}{\sin(\pi e)\sqrt{2-e^{-2\pi ie}}}.
 \tag{10}
\]
Write \(\Psi_{ee}=-A+iB\).
The exact angle estimates in Section 5 of the complete envelope
theorem apply on \(23/100\le\Re e\le7/20\),
\(-1/20\le\Im e\le0\), and give
\[
                  A>0,\qquad |B|<(8/31)A.
 \tag{11}
\]
We will additionally use the explicit lower bound
\[
                             A>15/2.
 \tag{12}
\]

Here is a direct witness for (12), on the same rectangle.
The first term in (10) has real part greater than
\[
                         \frac{640\pi}{441}.
 \tag{13}
\]
Indeed \(\sin(2\pi\Re e)>4/5\), and
\[
 |\sin(2\pi e)|^2
 \le\cosh^2(\pi/10)<(21/20)^2.
 \tag{14}
\]
For the last bound, the elementary series inequality
\[
 \cosh t\le1+\frac{t^2/2}{1-t^2/12}
 \qquad(0\le t<\sqrt{12})
\]
and \(t=\pi/10<11/35\) give
\[
 \cosh(\pi/10)<1+\frac{726}{14579}<\frac{21}{20}.
 \tag{15}
\]
The real numerator of \(1/\sin(2\pi e)\) is
\(\sin(2\pi\Re e)\cosh(2\pi\Im e)>4/5\).
This proves (13).

For the second term of (10),
\[
 |\sin\pi e|<21/20,\qquad
 |\sqrt{2-e^{-2\pi ie}}|<7/4.
 \tag{16}
\]
The first follows from (14) with half its height, and the
second from \(|e^{-2\pi ie}|\le1\) and \(\sqrt3<7/4\).
The same denominator argument used for (11) has modulus
less than \(1/4\). Since \(\cos(1/4)>31/32\), the real
part of that second term is greater than
\[
              2\pi\frac{31/32}{(21/20)(7/4)}
                         =\frac{155\pi}{147}.
 \tag{17}
\]
Adding (13) and (17), and using \(\pi>25/8\), gives
\[
                   A>\frac{1105\pi}{441}>
                        \frac{27625}{3528}>\frac{15}{2}.
 \tag{18}
\]
All bounds concern the original selected square root.

For the affine parametrization of the joining segment, (9)--(12)
now imply
\[
 \Re\{\Psi_{ee}(\Delta E+i\Delta h)^2\}
 <-A(\Delta E)^2
       \left(1-\frac1{100}-\frac8{155}\right)
 =-A(\Delta E)^2\frac{2909}{3100}.
 \tag{19}
\]
The first derivative vanishes at the actual original saddle
\(e_+\). Integrating twice along the segment therefore gives
\[
 \boxed{\quad
 M_{\mathrm{half}}-R_d(1/2)>
       \frac{43635}{1240000}>\frac1{30}.
 \quad}
 \tag{20}
\]
The first rational bound is
\((1/2)(15/2)(1/100)(2909/3100)\).
For the second, \(30\cdot43635-1240000=69050>0\).
This is an explicit gap for the original absolute actions,
not a numerical estimate of either action separately.

## 3. The departure remains below the stronger affine envelope

Put \(d=a-1/2\). Equations (5)--(11) of
[the exact multiplier-decrease theorem](research_mixed_next_cap_multiplier_decrease.md)
give
\[
 R_d'(a)<
 -\log(3/2)-\frac{11\pi}{20}d
                         -\frac{121\pi^2}{400}d^2.
 \tag{21}
\]
In particular, integrating and retaining only the quadratic
improvement, (20) yields
\[
 R_d(a)<
 M_{\mathrm{half}}-\frac1{30}
             -\log(3/2)d-\frac{11\pi}{40}d^2.
 \tag{22}
\]
For every \(d\ge0\),
\[
\begin{split}
 \log(4/3)d-\frac{11\pi}{40}d^2
 &<\frac13d-\frac{55}{64}d^2\\
 &\le\frac{16}{495}
    =\frac1{30}-\frac1{990}.
\end{split}
\tag{23}
\]
The first inequality uses \(\log(1+1/3)<1/3\) and
\(\pi>25/8\); at \(d=0\) its non-strict form suffices.
The second is the exact maximum of the displayed real quadratic.
Combining (22)--(23) proves the uniform strict departure estimate
\[
 R_d(a)<
 M_{\mathrm{half}}-\log2\,(a-1/2)-\frac1{990},
               \qquad 1/2\le a\le7/10.
 \tag{24}
\]
Equation (5) controls the other branch of the maximum in (1).
Consequently
\[
 \boxed{\quad
 \mathcal E(a)\le
 M_{\mathrm{half}}-\log2\,(a-1/2)
                  \qquad(1/2\le a\le7/10).
 \quad}
 \tag{25}
\]
This compares both actions with one affine upper envelope.
It does not assert \(R_d(a)\le M(a)\), which the fixed-departure
obstruction disproves at \(a=7/10\).

## 4. Complete finite-source conclusion and scope

**Theorem.** For every \(\tau>0\), uniformly on the whole real
incoming arc and along both integer parities,
\[
 |U_{0,N}(-2,e^{-2\pi ia})|
 \le C_\tau N^{B_\tau}
   \exp N\{M_{\mathrm{half}}-\log2\,(a-1/2)+\tau\}.
 \tag{26}
\]
The original half-face action may be replaced by the established
upper bound
\[
        M_{\mathrm{half}}<
        \widehat M=\frac{203}{200}-\frac{1303}{7680000}.
 \tag{27}
\]
The same fixed-base small complex ordinary-color/incoming
neighborhoods and all fixed mixed derivatives are available,
with arbitrarily small additional rate and polynomial costs.

Indeed (26) is (4) with its now strengthened upper rate (25).
The complete finite interpolation, the original \(+N\) residue
density, physical index sets, all six weighted currents and
every unweighted main join are exactly those already controlled
in that theorem. No new region of endpoint-source continuation
is assumed. The neighborhoods and derivative assertions follow
from the same fixed contours and Cauchy estimates, after a
common shrink for the requested tolerance.

This improves the cap factor available for the actual following
selected comparison. It does not by itself assign a sign to
the full following density, pay its initial vertical connector,
or assert a nonzero complete cap coefficient on the whole arc.
The main-path color scope remains complete color and its small
complex neighborhood; no all-real-color main estimate is inferred.
