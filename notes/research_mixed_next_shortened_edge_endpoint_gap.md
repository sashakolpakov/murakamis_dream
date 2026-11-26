# A strict right-end gap for the shortened second edge

Private written source estimate, 8 November 2026. No mathematical
numerical evaluation, saved-value calculation, or frozen-source edit
is used.

The original edge action exceeds the physical half-endpoint rate
by more than \(1/25\) on a fixed two-angle box containing the
continued cubic family. The proof retains the original closed
derivative form and its additive constant. Uniform finite product
bounds then pay a fixed terminal interval of the shortened second
edge, at both level parities. The intervening right wire interval
and the right cut of the first-quarter contour remain unestimated.

## 1. A common original phase on a fixed two-angle box

Consider
\[
 \mathcal Q=
 \left\{(t,u):
 \begin{array}{c}
 t=a-iH,\quad u=b-iK,\quad 0\le a,b\le\pi/2,\\
 0\le H\le1,\quad 0\le K\le1/2
 \end{array}\right\}.
 \tag{1}
\]
Keep the original edge derivative and complete constant from
[the bare-edge source, Section 1](research_bare_kernel_thin_rectangle.md):
\[
 \begin{split}
 r_t(t,u)&=\operatorname{arsinh}
              \{\tan(t/2)\cos(u/2)\},\\
 r_u(t,u)&=\operatorname{arsinh}
              \{\tan(u/2)\cos(t/2)\},\\
 d\psi&=-\pi^{-1}(r_t\,dt+r_u\,du),\qquad
                     \psi(0,0)=-8J(1/4),\\
 J(x)&=\int_0^x\log(2\sin\pi s)\,ds\quad(0\le x\le1).
 \end{split}
 \tag{2}
\]
The inverse hyperbolic sines in this note are their principal
branches, calibrated to the original germ.

**Lemma 1.** The one-form in (2) is holomorphic and closed on
a fixed complex neighborhood of \(\mathcal Q\). Its primitive
there is the analytic continuation of the original edge phase.
On \(\mathcal Q\),
\[
             \Re r_t,\Re r_u\ge0,\qquad
             -\pi/2<\Im r_t,\Im r_u<\pi/2.
 \tag{3}
\]

*Proof.* The arguments of the two inverse hyperbolic sines
avoid the principal cuts. Indeed
\[
 \tan(t/2)=\frac{\sin a-i\sinh H}{\cos a+\cosh H},
 \qquad
 \cos(u/2)=
 \cos(b/2)\cosh(K/2)+i\sin(b/2)\sinh(K/2).
 \tag{4}
\]
Their product \(z_t\) has real part
\[
 \Re z_t=
 \frac{\sin a\cos(b/2)\cosh(K/2)
             +\sinh H\sin(b/2)\sinh(K/2)}
      {\cos a+\cosh H}\ge0.
 \tag{5}
\]
The same calculation with the arguments interchanged gives
\(\Re z_u\ge0\). If \(\Re z_t=0\), then \(a=0\), and its
possible purely imaginary value satisfies
\[
 |z_t|\le\tanh(1/2)\cosh(1/4)
                       <\sinh(1/2)<1.
 \tag{6}
\]
If \(\Re z_u=0\), the analogous bound is
\[
 |z_u|\le\tanh(1/4)\cosh(1/2)
                       <\sinh(1/2)<1.
 \tag{7}
\]
For an elementary witness,
\(\sinh(1/2)<\tfrac12\cosh(1/2)<4/7\), using the existing
positive-series bound \(\cosh(1/2)<8/7\).
Thus neither argument meets the cuts \(i[1,\infty)\) and
\(-i[1,\infty)\). On the closed right half-plane with these
cuts excluded, the principal inverse hyperbolic sine has
nonnegative real part and imaginary part in \((-\pi/2,\pi/2)\).
This proves (3). Compactness supplies a common complex
neighborhood on which both returns are holomorphic.

The two cosine denominators are nonzero there. Put
\[
 \Delta=1-\sin^2(t/2)\sin^2(u/2),
\]
\[
 Q_t=\cos(t/2)\sqrt{1+z_t^2},\qquad
 Q_u=\cos(u/2)\sqrt{1+z_u^2},
 \tag{8}
\]
where the square roots are those occurring in the derivatives
of the specified inverse hyperbolic sines.
Both functions are nonzero and their squares equal \(\Delta\).
They agree at \((0,0)\), so they agree throughout a connected
neighborhood of \(\mathcal Q\). Therefore
\[
 \partial_u r_t
   =-\frac{\sin(t/2)\sin(u/2)}{2Q_t}
   =\partial_t r_u .
 \tag{9}
\]
Choose that neighborhood convex and small enough to retain all
the cut and denominator guards. Equation (9) proves that (2)
has a holomorphic primitive. Its specified constant and its
derivatives agree with the original edge phase near completeness,
so it is that phase's uniquely calibrated continuation.
No logarithm or additive constant is reset. \(\square\)

## 2. A quantitative action comparison with the half endpoint

Define the real function
\[
 G(a,H,b,K)=\Re\psi(a-iH,b-iK)-\frac{H+K}{2}.
 \tag{10}
\]

**Theorem 2.** Uniformly on the entire box (1),
\[
 \boxed{\qquad
 \Re\psi(t,u)-\frac{H+K}{2}>
                 \frac{11}{252}>\frac1{25}.
 \qquad}
 \tag{11}
\]

*Proof.* Lemma 1 gives
\[
 \partial_aG=-\frac{\Re r_t}{\pi}\le0,\qquad
 \partial_bG=-\frac{\Re r_u}{\pi}\le0,
\]
\[
 \partial_HG=-\frac{\Im r_t}{\pi}-\frac12<0,\qquad
 \partial_KG=-\frac{\Im r_u}{\pi}-\frac12<0.
 \tag{12}
\]
It follows that the minimum is attained at the corner
\[
                   t=\pi/2-i,\qquad u=\pi/2-i/2.
 \tag{13}
\]
The value of \(\Re\psi\) at that corner is at least its value
at the corresponding real corner. To see this without replacing
the action by an independent modulus, follow the path
\[
           t_\tau=\pi/2-i\tau,\qquad
           u_\tau=\pi/2-i\tau/2,\qquad 0\le\tau\le1.
 \tag{14}
\]
At positive \(\tau\), formulas (4) give exactly
\[
 \begin{split}
 \Im z_t(t_\tau,u_\tau)
   &=\frac{\cosh(\tau/4)}{\sqrt2\,\cosh\tau}
                       \{\tanh(\tau/4)-\sinh\tau\}<0,\\
 \Im z_u(t_\tau,u_\tau)
   &=\frac{\sinh(\tau/2)}{\sqrt2}
                       \{\operatorname{sech}(\tau/2)-1\}<0.
 \end{split}
 \tag{15}
\]
Their real parts are positive, so the principal returns have
negative imaginary parts as well. Consequently
\[
 \frac{d}{d\tau}\Re\psi(t_\tau,u_\tau)
                =-\pi^{-1}\{\Im r_t+\tfrac12\Im r_u\}>0.
 \tag{16}
\]

At the real corner, the original wire saddle is \(y=1/6\).
This follows either from the original critical equation or from
\(\cos(2\pi y)=1/2\) when \(\cos t=\cos u=0\).
The calibrated real Newton phase therefore gives
\[
 \begin{split}
 \psi(\pi/2,\pi/2)
 &=2\left\{
       \int_0^{1/6}\log(2\cos(2\pi s))\,ds-2J(1/6)
       \right\}\\
 &=-5J(1/6).
 \end{split}
 \tag{17}
\]
For the last equality, if
\(L(x)=\int_0^x\log(2\cos\pi s)\,ds\) on \([0,1/2)\),
then \(L(x)=J(x+1/2)\), \(J(1/2)=0\), and
\(J(5/6)=-J(1/6)\). Thus the integral in braces before
subtracting \(2J(1/6)\) is \(-J(1/6)/2\).
All real factorial arguments at this saddle are positive,
so this evaluation uses the original phase constant.

The elementary sine bound supplies a strict rational witness:
\[
 \begin{split}
 -J(1/6)
 &>\frac16\{1-\log(\pi/3)\}\\
 &>\frac16\left(1-\frac1{21}\right)
     =\frac{10}{63},
 \end{split}
 \tag{18}
\]
because \(2\sin\pi s<2\pi s\),
\(\pi/3<22/21\), and \(\log(22/21)<1/21\).
This is the same written witness as equation (18) of
[the original Newton-envelope calculation](research_mixed_next_three_outer_mode_newton_envelope_obstruction.md);
it requires no evaluation of the continued critical point.
Combining (12)--(18) gives
\[
 G(t,u)\ge G(\pi/2-i,\pi/2-i/2)
     >\frac{50}{63}-\frac34=\frac{11}{252}.
 \tag{19}
\]
Finally \(11/252-1/25=23/6300>0\). \(\square\)

## 3. Application to the actual shortened second edge

Now let \(t=t(u)\) be the original cubic branch on
\[
             \mathcal U_+
       =\{u=a-ih:0\le a\le\pi/2,\ 0\le h\le1/2\}.
 \tag{20}
\]
The [cubic continuation theorem](research_mixed_next_inner_three_cubic_continuation.md)
places this compact family strictly inside the \(t\)-bounds of
(1), with \(0<\Re t<\pi/2\) and \(0<-\Im t<1\).
The action in Lemma 1 agrees here with the original wire action
of [the first-quarter source reduction](research_mixed_next_two_angle_bare_first_quarter_contour.md),
equation (14). Both use the same edge derivatives and complete
constant, and their continuation starts from the original
complete-outside edge. In particular the right side of (11)
is measured against that source's actual selected action.

Use the original Newton basis and the parity-exact cutoff of
[the exact shortened-edge reduction](research_mixed_next_outer_exact_low_edge_reduction.md):
\[
 \begin{gathered}
 D=N-1,\qquad U=\lfloor N/2\rfloor-1,\qquad
 S_j=\prod_{\nu=1}^j2\sin(\pi\nu/N),\\
 e_j(\xi)=S_j^{-2}
     \prod_{\nu<j}\{2\cos((2\nu+1)\pi/N)-\xi\},\\
 K_N^{<}(t,u)=
       \sum_{j=0}^{U}e_j(-2\cos t)e_j(-2\cos u).
 \end{gathered}
 \tag{21}
\]
For any bounded complex angle \(a\), retain its original
physical-row upper rate
\[
 V_a(x)=
  \int_0^x\log|2\cos(2\pi s)+2\cos a|\,ds-2J(x),
                    \qquad 0\le x\le1/2.
 \tag{22}
\]
The exact midpoint numerator estimate and the original
sine-factorial estimate give, uniformly on the compact family,
\[
 |e_j(-2\cos t)e_j(-2\cos u)|
    \le C N^A
        e^{N\{V_t(j/N)+V_u(j/N)\}}.
 \tag{23}
\]
These are the zero-safe finite product estimates in
[real-period Newton, Lemma 1](research_three_crossing_real_period_newton_bound.md)
and [the complete complex Newton bound, Section 2](research_mixed_next_physical_three_kernel_fourier_bound.md).
The same proof applies on any fixed bounded height range:
remove the bounded number of cells nearest a shifted cosine
zero, estimate the remaining derivative errors by a harmonic
sum, and use the scaled logarithmic integral on each removed
cell. Its upper error is \(O(\log N)\) uniformly, including
exact numerator zeros and both level parities. No relative
factorial expansion through a zero is being asserted.

The exact endpoint identity is
\[
             V_a(1/2)=\frac{|\Im a|}{2}.
 \tag{24}
\]
Indeed the full-period mean of the numerator logarithm is
\(|\Im a|\), by its two circle factors. Its reflection symmetry
halves that value on \([0,1/2]\), and \(J(1/2)=0\).
It follows that the rate at the physical half-endpoint in (23)
is precisely \((H_t+h)/2\).

The integrated logarithms in (22) are jointly continuous
through their zeros on the present compact parameter family.
For example, splitting at distance \(\epsilon\) from each
shifted sine zero gives the familiar uniform modulus
\(O(\epsilon|\log\epsilon|)\) for its local primitive; away
from those neighborhoods it is uniformly continuous.
Hence there is a fixed \(\delta\in(0,1/12)\) such that
\[
 V_{t(u)}(x)+V_u(x)
       \le\frac{H_t+h}{2}+\frac1{100}
       <\Re\psi(t(u),u)-\frac3{100}
 \tag{25}
\]
for every \(u\in\mathcal U_+\) and
\(1/2-\delta\le x\le1/2\).
Only continuity of the real upper rate is used; no contour
or local relative packet is extrapolated to these rows.

**Theorem 3.** For some fixed \(\delta\in(0,1/12)\), all
sufficiently large levels of either parity satisfy
\[
 \boxed{\quad
 \sum_{j=\lceil N(1/2-\delta)\rceil}^{\,\lfloor N/2\rfloor-1}
   |e_j(-2\cos t(u))e_j(-2\cos u)|
       \le C e^{N\{\Re\psi(t(u),u)-1/50\}},
                 \qquad u\in\mathcal U_+ .
 \quad}
 \tag{26}
\]
The same estimate holds for every subset of the displayed
indices. Empty sums have value zero.

*Proof.* Sum (23) using (25), retaining the at most \(N\)
original terms. The resulting fixed polynomial cost is absorbed
in the reserve between \(3/100\) and \(1/50\).
The upper cutoff in (26) is exactly the adopted shortened
edge cutoff at both parities; it omits the odd middle row only
because that row was removed by the original outer annihilator,
not by a new asymptotic assertion. \(\square\)

This is a bound for an actual positive finite block of the
unchanged shortened edge. It adds no trace scalar or extra
factor of \(N\); any later cotangent or trace operation retains
its own original normalization.

## 4. Remaining scope

The theorem pays a fixed right physical endpoint interval,
independently of the reflected-ray comparison that fails
near that endpoint. It does not prove a gap at the real
wire face \(x=1/3\), or at the right cut of the existing
first-quarter contour. The intervening original physical
indices, their possible coherent contour replacement, and
the complete inner and outer trace estimates remain separate.

No full packet for \(K_N^{<}(t,u)\), no nonzero coefficient
for its complete finite sum, no inner three-kernel packet,
and no full-transfer or knot-family conclusion is asserted.
