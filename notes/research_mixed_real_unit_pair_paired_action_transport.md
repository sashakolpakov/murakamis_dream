# Comparing the critical action by moving the second coordinate

Private written proof, 11 November 2026. Author-frozen for separate
proof and direct-source review; not adopted.

For the missing real first interval, it is unnecessary to assume that
the conditional critical action decreases with the first coordinate.
One can instead move the second coordinate back to one half, keeping
the first coordinate fixed. The critical action and each of the three
horizontal comparison rates for the following type-three factor
decrease together. The small possible increase of that following
factor is paid by a strict decrease of the conditional action.

This is a comparison of action functions. It is not an estimate for
the complete first conditional polynomial.

## 1. The functions being compared

Use the original primitive and the two conditional phases
\[
 g'(w)=\operatorname{Log}(1-e^{-2\pi i w}),\qquad
 Q_\epsilon(s;a,q)=g(s+a)+g(s+q)-(2+\epsilon)g(s)
                  -g(a)-g(q)+2\pi ias .
 \tag{1}
\]
Every logarithm has its original branch on \(0<\Re w<1\).
No additive constant or Fourier carrier is changed.

Throughout this note,
\[
 \frac12\le a\le\frac78,\qquad
 \frac12\le q\le\frac{18}{25}.
 \tag{2}
\]
The [zero-lift theorem](research_mixed_real_unit_pair_zero_lift_branch.md)
gives a unique solution \(s=t+i\eta\) of
\[
 Q_{1,s}(s;a,q)=0,\qquad
 0<t<\min(1-a,1-q),\qquad \eta<0 .
 \tag{3}
\]
Define its original critical action by
\[
                   \Theta(a,q)=Q_1(s(a,q);a,q).
 \tag{4}
\]
It is holomorphic near the compact real rectangle (2).

For the following type-three factor, fix
\[
 z=b+ic_3,\quad
 \frac{11}{50}\le b\le\frac9{20},\quad
 -\frac{13}{200}\le c_3\le\frac{17}{250}.
 \tag{5}
\]
Choose the same cuts as in the
[paired-current theorem](research_mixed_443_paired_upper_prewall_currents.md):
the fixed \(r_0<1/2\) is sufficiently close to \(1/2\), and
\[
 0<\varepsilon<\frac1{40},\qquad
 r(q)=\min\{r_0,1-q-\varepsilon\},\qquad
 I_q=[1/8,r(q)] .
 \tag{6}
\]
In particular \(r_0>21/100\), and every interval used below has
positive length. For
\[
 \sigma\in[-13/200,17/250]\quad\hbox{or}\quad \sigma=1/5
\]
put
\[
              B_\sigma(q,z)=
                  \max_{u\in I_q}\Re Q_0(u+i\sigma;q,z).
 \tag{7}
\]
These are the unchanged main or sampling-correction profiles.
Their constant penalties may be subtracted on both sides of any
comparison below.

**Theorem 1.** For every choice in (2), (5)--(7),
\[
 \Re\Theta(a,q)+B_\sigma(q,z)
       \le \Re\Theta(a,1/2)+B_\sigma(1/2,z).
 \tag{8}
\]
Also \(\Re\Theta(a,q)\) is nonincreasing in \(q\).
Neither assertion assumes a sign for
\(\partial_a\Re\Theta(a,q)\) when \(q>1/2\).

## 2. The radius and the early real-index bound

Write \(\rho=e^{2\pi\eta}\), so \(0<\rho<1\). For \(0<u<1\),
let
\[
       \alpha_\rho(u)=\Arg(1-\rho e^{-2\pi i u}).
\]
Its absolute value is at most \(\arcsin\rho\). The imaginary
part of (3) is
\[
 \alpha_\rho(a+t)+\alpha_\rho(q+t)-3\alpha_\rho(t)+2\pi a=0.
 \tag{9}
\]
If \(\rho\le1/2\), its left side is at least
\(\pi-5\pi/6=\pi/6>0\). Consequently
\[
                              \frac12<\rho<1.
 \tag{10}
\]
This also gives the height bound
\(-\log2/(2\pi)<\eta<0\) throughout (2).

For the initial second interval we need a quantitative real-index
bound:
\[
      t>\frac2{25}\qquad\left(\frac12\le q\le\frac{21}{40}\right).
 \tag{11}
\]
Suppose instead that \(0<t\le2/25\), and set
\[
 \begin{split}
 A&=|1-\rho e^{-2\pi i(a+t)}|^2,\\
 B&=|1-\rho e^{-2\pi i(q+t)}|^2,\\
 D_s^2&=|1-\rho e^{-2\pi it}|^2 .
 \end{split}
\]
The incoming angle belongs to \([1/2,191/200]\), so
\[
 A>(1-\rho)^2+\frac{\rho}{16}
   =(\rho-31/32)^2+\frac{63}{1024}
   \ge\frac{63}{1024}.
 \tag{12}
\]
Here \(\sin(9\pi/200)>1/8\). For a direct witness, use
\(\pi>3\) and
\(\sin(27/200)\ge27/200-(27/200)^3/6>1/8\).

The outgoing angle belongs to \([1/2,121/200]\); its cosine
is negative. Hence
\[
                         B>1+\rho^2>\frac54.
 \tag{13}
\]
The own angle satisfies \(\sin(2\pi/25)<1/4\), giving
\[
 D_s^2<(1-\rho)^2+\frac{\rho}{4}\le\frac38.
 \tag{14}
\]
The final inequality follows by convexity on \(1/2\le\rho\le1\).
One exact witness for the sine bound is
\(\sin x\le x-x^3/7\) on \(0\le x\le1\), obtained from
the alternating sine series. This polynomial increases on that
interval, and its value at \(44/175>2\pi/25\) is less than
\(1/4\): subtracting \(1/4\) from \(44/175\) gives \(1/700\),
whereas \((44/175)^3/7>1/700\).

At a critical point the modulus of the exponentiated equation is
\[
                                AB=D_s^6 .
 \tag{15}
\]
Equations (12)--(14) instead give
\[
          AB>\frac{315}{4096}>\frac{216}{4096}
                    =\frac{27}{512}>D_s^6.
 \tag{16}
\]
This contradiction proves (11).

## 3. Decrease with the second coordinate

Put
\[
 D(q)=|1-e^{-2\pi iq}|,\qquad
 N_2=|1-\rho e^{-2\pi i(q+t)}|.
\]
Stationarity in (3), with the original logarithms, gives
\[
                  \partial_q\Re\Theta=\log(N_2/D(q)).
 \tag{17}
\]
Since \(q<5/6\), \(D(q)>1\). Also \(q<q+t<1\), so
\(\cos2\pi(q+t)\ge\cos2\pi q\). Convexity of
\(1+\rho^2-2\rho\cos2\pi(q+t)\) in \(0\le\rho\le1\)
reduces its upper bound to the two endpoints. Both are at most
\(D(q)^2\). Therefore
\[
                              N_2\le D(q).
 \tag{18}
\]
This proves the separate monotonicity in Theorem 1.

On \(1/2\le q\le21/40\), (11) yields a stronger bound.
The shifted angle is greater than \(29/50\) and less than one.
Thus, again by convexity in \(\rho\),
\[
 N_2^2\le 2+2\cos(4\pi/25)<\frac{31}{8}.
 \tag{19}
\]
For the strict comparison, \(4\pi/25>\pi/8\) and
\(\cos(\pi/8)<15/16\); the latter follows by positive
squaring from \(\sqrt2<97/64\).

## 4. Pairing with the following maximum

Section 3 of the paired-current theorem supplies the following
statements about (7), independently of its preceding factor.
At any maximizing point \(u+i\sigma\), its derivative with
respect to \(q\), before endpoint motion, is
\[
 \log(N_3/D(q)),\qquad
                 N_3=|e^{-2\pi\sigma}-e^{-2\pi i(q+u)}|.
 \tag{20}
\]
For \(-13/200\le\sigma\le17/250\), it proves
\[
 \begin{array}{ll}
 N_3^2<81/20,\quad D(q)^2>159/40,
                                  &1/2\le q\le21/40,\\
 N_3\le D(q),                      &21/40\le q\le18/25.
 \end{array}
 \tag{21}
\]
These are bounds at every maximizing point. They include a
maximizer at the right endpoint. The proof first excludes
indices below \(\min\{21/100,(1-q)/2\}\), then uses the
original radius bounds and three explicit angular intervals.
For \(\sigma=1/5\), the same source gives \(N_3\le D(q)\)
throughout the whole second interval.

In the initial range, (19) and (21) imply
\[
 N_2^2N_3^2<\frac{31}{8}\frac{81}{20}
       =\frac{25110}{1600}
       <\frac{25281}{1600}
       =\left(\frac{159}{40}\right)^2<D(q)^4.
 \tag{22}
\]
Thus the sum of (17) and (20) is negative.
On the remaining range it is nonpositive by (18) and (21).
For the upper sampling profile \(\sigma=1/5\), (18) alone
combines with its pointwise third-factor inequality.

The maximum (7) is locally Lipschitz on its compact parameter
interval. At a maximizing right endpoint, the one-sided private
derivative is nonnegative; multiplication by \(r'(q)\le0\)
makes the endpoint-motion term nonpositive. The left endpoint
is fixed. Consequently the upper envelope derivative of
\(\Re\Theta+B_\sigma\) is nonpositive, including at a switch
between maximizing points. Integration, with the same one-sided
argument at the kink of \(r(q)\), proves (8).

## 5. Other third-factor comparisons and the remaining obligation

If \(L(q)\) is any nonincreasing real-cut or physical-row
comparison rate for the third factor, (18) immediately gives
\[
       \Re\Theta(a,q)+L(q)
              \le\Re\Theta(a,1/2)+L(1/2).
 \tag{23}
\]
The complete third-factor proof in Section 6 of the paired-current
source bounds its unweighted joins, weighted vertical pieces,
wall collar and physical rows by the three profiles (7) and
the original real-left, half and last comparison rates.
Those latter comparison rates are nonincreasing or constant
on this interval, as recorded also in Section 7 of the
[complete core-pair proof](research_mixed_443_core_first_complete_right_pair.md).
Thus (8) and (23) can be applied to each of that proof's retained
third-factor alternatives. Constant sampling penalties cancel
between the two sides.

The result changes the direction of the comparison: first return
the second coordinate to one half, with the following factor
attached. Any already proved half-face comparison may then be
used at that same first coordinate. It does not require extending
a first-coordinate action monotonicity statement beyond its
proved outgoing domain.

There remains an essential distinction. The first conditional
polynomial is a complete finite sum. The present proof bounds
its chosen critical action, not its other sampling corrections,
its unweighted joins or its physical rows beyond either
numerator wall. Until those terms are estimated, replacing that
polynomial by \(e^{N\Theta}\) is unjustified. In particular the
extra algebraic root with logarithmic value \(-2\pi i\) has
not been removed from the finite problem. No whole-period
asymptotic or new knot-volume theorem is asserted here.

## Direct source versions

| Direct source | Implication used | SHA-256 |
|---|---|---|
| research_mixed_real_unit_pair_zero_lift_branch.md | Original zero-lift branch, negative height, nondegeneracy and parameter regularity | 4e22a14247e7b11340d9b9ade4774760cd93722f82feb16c12ff2faa1c2b4d1a |
| research_mixed_443_paired_upper_prewall_currents.md | Third maximizing-index bounds, moving-endpoint derivative and complete third-factor comparisons | 9b851f2e88f14be3116be661d8377bae514c77c28fbe594011b5966acc4ea77e |
| research_mixed_443_core_first_complete_right_pair.md | Explicit separation of the complete third-factor alternatives and their monotonicity | 3f3fa659048dd5961e54a29d71bdcd6e6b73bd4927e4d802ffa8e0849b86cd21 |

This note uses written inequalities. It introduces no mathematical
numerical evaluation, test, import or compilation, and changes no
frozen source.
The author has read the entire final proof and all three directly
used source implications, including the third-factor maximizing
arguments and complete contour inventory. The three source
bindings have been checked. Separate review remains required.
