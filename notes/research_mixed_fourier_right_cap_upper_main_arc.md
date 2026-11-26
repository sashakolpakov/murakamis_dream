# The paid right-hand complement of the joint right-cap main contour

Research deduction, 7 November 2026. On the original negative
critical heights, the joint main-sheet rate strictly decreases as
the outgoing real coordinate moves from \(9/20\) to \(3/4\).
A half-period comparison pays the remaining interval to one.
The existing sheet estimate therefore pays this entire right-hand
part of the main complement. A global lower-half-plane
factorial symbol justifies the estimate even where the real part
of the numerator argument crosses the old support wall.

This is a bound for one part of the joint central-index main
current. It is not a pointwise bound for the complete truncated
conditional factor or a bound for its vertical boundary current.
No numerical evaluation is used.

## 1. The original factorial symbol across a positive real wall

Use the exact \(\Pi_N\) and its continuation from
[the joint global chart](research_mixed_fourier_right_cap_joint_global_chart.md).
For \(\Im z<0\), define
\[
 w=e^{-2\pi iz},\qquad
 g_-(z)=\frac{\operatorname{Li}_2(w)-\pi^2/6}{2\pi i},
 \qquad
 A_-(z)=e^{-i\pi/4}\exp\{\tfrac12\Log(1-w)\}.
 \tag{1}
\]
The logarithm and dilogarithm are their disk series. On the
original regular strip these are exactly the original \(g\)
and \(A(z)=\sqrt{2\sin\pi z}\,e^{-\pi iz/2}\), with their
original branches.

**Lemma 1.** On every compact subset of \(\Im z<0\),
\[
 \Pi_N(z)=N^{1/2}A_-(z)e^{Ng_-(z)}
                                      (1+O(N^{-1})),
 \tag{2}
\]
uniformly with every fixed derivative of the normalized error.
There is no restriction on \(\Re z\).

*Proof.* The exact normalized
[cyclotomic formula](research_exact_cyclotomic_factorial.md),
equations (7)--(9), gives
\[
 \begin{split}
 \log\Pi_N(z)
 &=\tfrac12\log N+i\pi\left(\frac N{12}-\frac14+\frac1{12N}\right)
                                      +\mathcal E_N(z),\\
 \mathcal E_N(z)
 &=z\Log(1-w^N)
  -\sum_{\substack{m\ge1\\N\nmid m}}
                  \frac{w^m}{m(1-e^{2\pi im/N})}
  +\sum_{\substack{m\ge1\\N\mid m}}\frac{N-1}{2m}w^m
  +\frac{i}{2\pi N}\operatorname{Li}_2(w^N).
 \end{split}
 \tag{3}
\]
For the second identity, expand its finite weighted logarithmic
sum and use
\(\sum_{k=0}^{N-1}k e^{2\pi ikm/N}=-N/(1-e^{2\pi im/N})\)
off the resonances and \(N(N-1)/2\) at them.
These manipulations converge absolutely because \(|w|<1\).

For \(1\le m\le N/2\),
\[
 -\frac1{1-e^{2\pi im/N}}
       =\frac N{2\pi im}-\frac12+O(m/N).
 \tag{4}
\]
The remainder is uniform on that interval after the removable
singularity at zero is subtracted. For the remaining
nonresonant terms use
\(|1-e^{2\pi im/N}|\ge4/N\).
On a compact set \(|w|\le r<1\), all tails beyond \(N/2\),
all resonant terms and the \(z\Log(1-w^N)\) term are
exponentially small times a polynomial in \(N\).
Summing (4) therefore gives
\[
 \mathcal E_N(z)=
       \frac N{2\pi i}\operatorname{Li}_2(w)
            +\frac12\Log(1-w)+O(N^{-1}).
 \tag{5}
\]
The original constant in (3) now proves (2).
Cauchy's formula on a slightly larger compact set proves
the normalized derivative statement. No interpolation is
identified through its lattice values alone. \(\square\)

In particular a negative-height numerator can pass through
\(\Re z=1\) in (2). Its actual zeros are on the real line;
none lie on the compact lower-half-plane domain of this lemma.

## 2. The exact main phase on the upper outgoing arc

Keep the actual reference, heights and incoming allocation of
[the bare inner-contour theorem](research_mixed_fourier_right_cap_bare_inner_contour.md):
\[
 \begin{gathered}
 \eta\in\{0,1\},\quad a_*\in K_{3+\eta},\quad
 (s_*,q_*)\in O_4^2,\quad y=x_0,\quad Y=e^{2\pi iy},\\
 a=x+ih_a,\quad x\in P=[11/50,9/20],\quad h_a=\Im a_*,\\
 s=v+ih_s,\quad h_s=\Im s_*,\quad 1/8\le v\le1/2,\\
 q=z+ih_q,\quad h_q=\Im q_*,\quad 9/20\le z\le1,\\
 -.102\le h_s,h_q\le-.001 .
 \end{gathered}
 \tag{6}
\]
When \(\eta=1\), the incoming height is its original negative
unselected height. Write
\[
 S=e^{-2\pi is},\qquad Q=e^{-2\pi iq},\qquad \rho=|Y|.
 \tag{7}
\]
In particular \(|S|<1\) and \(|Q|<1\).

The exact joint source \(T_N\) is equation (10) of the
joint global chart. On (6), its phase, after the same
incoming halfweight is allocated, is
\[
 \mathscr F_\eta(s,a,q)=
 g(s+a)+g_-(s+q)-3g_-(s)
 -(1+\eta/2)g(a)-g_-(q)+2\pi ias+\ell_q(y).
 \tag{8}
\]
Here
\[
 \ell_q(y)=2\pi iy(q-\tfrac12)
 -\frac{\operatorname{Li}_2(YQ)-\operatorname{Li}_2(Y)}{2\pi i}
 \tag{9}
\]
is the original lifted cardinal phase. Every \(g_-\) in (8)
has a strictly negative imaginary argument. The other
factorial arguments remain in their original regular
strips: \(a_R\in P\), \((s+a)_R\in[.345,.95]\).
Thus the old regular-strip expansion and Lemma 1 give a
uniform nonzero symbol on the whole domain (6).
The cardinal symbol also stays in its original disk domain,
since \(|YQ|<1\).

For clarity, before the incoming halfweight is applied, this
is the exact source expansion
\[
 T_N(s,q;a,y)
   =N^{-5/2}\mathfrak b(s,a,q,y)
                  e^{N\mathscr F_0(s,a,q)}(1+O(N^{-1})),
 \tag{10}
\]
where
\[
 \mathfrak b=
 \frac{A(s+a)A_-(s+q)}
      {A(a)A_-(q)A_-(s)^3}\,
 \frac{e^{\pi iy}}{\sqrt{(1-Y)(1-YQ)}} .
 \tag{11}
\]
All roots have the stated original branches. The symbol is
nonzero and bounded on a neighborhood of (6). The incoming
finite factor is unchanged and independent of \(q\); its
same source bound from the bare inner-contour theorem
contributes \(-\eta\Re g(a)/2\). No outgoing halfweight is
inserted or divided out.

## 3. Monotonicity and the already paid face

**Proposition 2.** On (6) with \(9/20\le z\le3/4\),
\[
                    \Re\mathscr F_{\eta,q}<-1/10 .
 \tag{12}
\]

*Proof.* Differentiating the original disk primitives, with
no logarithmic reset, gives
\[
 \Re\mathscr F_{\eta,q}
 =\log\frac{\rho\,|1-SQ|}
                   {|1-Q|\,|1-YQ|}.
 \tag{13}
\]
For \(z\in[9/20,3/4]\), \(\cos(2\pi z)\le0\).
Also the original \(.18299<\Re y<.18301\) implies
\[
               -3\pi/2<\arg Y-2\pi z<-\pi/2,
 \tag{14}
\]
so \(\cos(\arg Y-2\pi z)<0\).
With \(R=|Q|<1\), it follows that
\[
 |1-SQ|\le1+R,\qquad
 |1-Q|\ge\sqrt{1+R^2},\qquad |1-YQ|>1.
 \tag{15}
\]
Consequently the ratio in (13) is less than
\[
             \rho\sqrt2<\frac58\sqrt2<\frac9{10}.
 \tag{16}
\]
The last comparison follows by squaring positive quantities.
Finally \(\log(9/10)<-1/10\). This proves (12),
including where \(\Re(s+q)\) crosses one. \(\square\)

Retain the original quantities
\[
 M_\eta=\Re\mathscr F_\eta(s_*,a_*,q_*),\qquad
 p_\eta=\Re\mathscr F_{\eta,a}(s_*,a_*,q_*),\qquad
 \kappa=1/2500000,
 \tag{17}
\]
and put
\[
 B_\eta(x)=M_\eta+p_\eta(x-\Re a_*)
                              -\kappa(x-\Re a_*)^2 .
 \tag{18}
\]
At \(z=9/20\), (8) is the original regular phase. Equation
(15) of the bare inner-contour theorem gives, for every
retained \(v\),
\[
 \Re\mathscr F_\eta(v+ih_s,a,9/20+ih_q)
 \le B_\eta(x)
       -\kappa(v-\Re s_*)^2-\kappa(9/20-\Re q_*)^2.
 \tag{19}
\]
The original \(O_4\) image has \(\Re q_*\le.36\), so define
the strictly positive uniform constant
\[
                    \delta_Q=\kappa(9/100)^2 .
 \tag{20}
\]
For \(9/20\le z\le3/4\), integrating (12) from this same face proves
\[
 \boxed{\quad
 \Re\mathscr F_\eta(v+ih_s,a,z+ih_q)
 \le B_\eta(x)-\delta_Q
       -\kappa(v-\Re s_*)^2-\frac{z-9/20}{10}.
 \quad}
 \tag{21}
\]
No physical-height row or complete outgoing group was substituted
for the joint main sheet in (19).

## 4. The remaining quarter-period

For \(\Im z<0\), define the original disk-branch difference
\[
 G(z)=g_-(z)-g_-(z+1/2),\qquad
 F_R(u)=\Re G\!\left(u+\frac{i\log R}{2\pi}\right),
                                      \quad 0<R<1.
 \tag{22}
\]
The primitive \(g_-\), and hence \(G\), has period one.
Writing \(E=Re^{-2\pi iu}\), differentiation gives
\[
 \partial_uF_R=
       \log\frac{|1-E|}{|1+E|},\qquad
 \partial_RF_R=
       \frac1{2\pi R}
       \Im\Log\frac{1+E}{1-E}.
 \tag{23}
\]
The fraction in the second formula lies in the right half-plane;
its imaginary part has the sign of \(\Im E\). Its indicated
logarithm is continued from \(R=0\), with no reset.
It follows that
\[
 \begin{array}{ll}
 -1/4\le u\le0:&F_R(u)\ge0,\quad
          \partial_uF_R(u)\le0,\quad\partial_RF_R(u)\ge0,\\
 0\le u\le1/2:&F_R(u)\le0 .
 \end{array}
 \tag{24}
\]
For the signs of \(F_R\), integrate the radial derivative
from its value zero at \(R=0\).

Suppose now \(3/4\le z\le1\), and put \(q_0=q-1\).
Then \(\Re q_0\in[-1/4,0]\), while
\(\Re(q_0+s)\in[-1/4,1/2]\).
If \(\Re(q_0+s)\ge0\), (24) gives
\(\Re G(q_0+s)\le0\le\Re G(q_0)\).
Otherwise its real coordinate is at least \(\Re q_0\),
and its radius is
\(e^{2\pi\Im(q_0+s)}\le e^{2\pi\Im q_0}\).
Both monotonicities in the first line of (24) then give the
same conclusion. Periodicity therefore proves
\[
 \Re\{g_-(s+q)-g_-(q)
              -g_-(s+q-1/2)+g_-(q-1/2)\}\le0 .
 \tag{25}
\]
This keeps the two incident factorial terms together.

The original cardinal contributes a strict gain. Put
\(t=|YQ|<5/8\). The odd terms of its absolutely convergent
dilogarithm series give
\[
 \begin{split}
 \Re\{\ell_q(y)-\ell_{q-1/2}(y)\}
 &\le-\pi\Im y+\frac1\pi
             \sum_{\substack{m\ge1\\m\ {\rm odd}}}\frac{t^m}{m^2}\\
 &\le-\pi\Im y+
              \frac1\pi\left(t+\frac{t^3}{9(1-t^2)}\right).
 \end{split}
 \tag{26}
\]
The lifted linear term is exactly \(\pi iy\); no output
periodicity is assumed. Since \(\rho<5/8\), the positive
atanh series gives
\[
 \pi\Im y=-\tfrac12\log\rho>
              \frac{1-\rho}{1+\rho}>\frac3{13}.
 \tag{27}
\]
The increasing bracket in (26) is less than \(235/351\).
Using \(\pi>3\), (26) is therefore strictly less than
\[
                 -\frac3{13}+\frac{235}{1053}
                      =-\frac{104}{13689}<-\frac1{200}.
 \tag{28}
\]

**Proposition 3.** For (6) with \(3/4\le z\le1\),
\[
 \Re\mathscr F_\eta(s,a,q)
       <\Re\mathscr F_\eta(s,a,q-1/2)-\frac1{200}.
 \tag{29}
\]
Indeed all the other terms of (8) are unchanged, so this is
(25) plus (28). The shifted coordinate \(z-1/2\) lies in
\([1/4,1/2]\). Up to \(9/20\), the original sheet estimate
in the bare inner-contour theorem applies; above \(9/20\),
use (21). Thus
\[
 \Re\mathscr F_\eta(v+ih_s,a,z+ih_q)
       \le B_\eta(x)-\kappa(v-\Re s_*)^2-\frac1{200}
                                      \quad(3/4\le z\le1).
 \tag{30}
\]
Combining (21) and (30), and using \(\delta_Q<1/200\), yields
the single bound
\[
 \boxed{\quad
 \Re\mathscr F_\eta(v+ih_s,a,z+ih_q)
       \le B_\eta(x)-\kappa(v-\Re s_*)^2-\delta_Q
                       \qquad(9/20\le z\le1).
 \quad}
 \tag{31}
\]

## 5. The corresponding finite main-current portion

Use the central retained half-grid endpoints \(\sigma_\pm\)
from the joint global chart, and \(\beta_N=1-1/(2N)\). Let
\[
 \mathcal I_N^{\rm upper}=
 N^2\int_{\sigma_-}^{\sigma_+}\int_{9/20}^{\beta_N}
            T_N(v+ih_s,z+ih_q;a,y)\,dz\,dv .
 \tag{32}
\]
This is a portion of the actual joint zero-mode contour, with
its original coefficient \(N^2\). The lower retained endpoint
differs from \(1/8\) by at most \(1/(2N)\); all symbols and
phase derivatives used above are bounded on a fixed nearby
compact set. This rounding changes the upper rate in (31)
by \(O(1/N)\), and therefore only changes a finite prefactor.

For every prescribed \(\tau>0\), the uniform symbols and the
unchanged incoming allocation give, for sufficiently large
levels of either parity,
\[
 |d_N(e^{-2\pi ia})|^{\eta/2}
       |\mathcal I_N^{\rm upper}|
 \le C_\tau N^{A_\tau}
               e^{N(B_\eta(x)-\delta_Q+\tau)} .
 \tag{33}
\]
One may in particular choose \(\tau<\delta_Q/2\).
All source normalizations in (10), (11) and (32) remain
those of the original cap.

The argument pays only this specified joint-main subregion.
It makes no assertion about the rest of its full-period
main path, the coherent sum of retained rows \(j<L_N\),
or the bounded-height part of the signed vertical current.
In particular it does not transport a modulus bound for
the complete conditional polynomial outside its proved
target strip. No new finite-source lower bound follows.
