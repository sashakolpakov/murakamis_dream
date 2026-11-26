# The complete first sum on a real second interval

Private written proof, 11 November 2026. Author-frozen for separate
proof and direct-source review; not adopted.

For a word beginning with powers \(4,4,3\), the first finite sum
can now be kept intact while the second coordinate ranges from
one half to \(18/25\). The new part of the argument is the
first real interval between one half and seven eighths. Its
complete conditional sum has two comparison rates. We bound
each of them with the full cap and the following factor attached.
The earlier estimates then close the first integration period.

## 1. The finite polynomial and the claimed bound

Fix the original geometric reference of an actual positive
three/four word of length at least four beginning with \(443\).
All heights, primitive constants and ordinary markings remain
those of the
[complete core-pair theorem](research_mixed_443_core_first_complete_right_pair.md).
In particular,
\[
 P=[11/50,9/20],\qquad z=b+ic_3,\quad b\in P,\qquad
 -13/200\le c_3,h_3\le17/250.
 \tag{1}
\]
Let \(c_1<0\), \(h_e<0\), and \(h_2<0\) be its actual first,
cap-index and first conditional-index heights. Set \(H=1/100\).

For \(\zeta=e^{-2\pi i/N}\), put
\[
 P_j=(\zeta;\zeta)_j,\quad p_j(V)=(\zeta V;\zeta)_j,\quad
 U_N(w,X)=\sum_{i<N}H_N(w,\zeta^{-i})p_i(X)/P_i^2,
\]
\[
 C_{\epsilon,N}(X,Y)=
       \sum_{j<N}X^{-j}p_j(X)p_j(Y)/P_j^{2+\epsilon}.
 \tag{2}
\]
Here \(H_N\) is the complete original endpoint polynomial.
The degree-\((N-1)\) interpolation polynomial \(d_N\) satisfies
\(d_N(\zeta^k)=P_k^{-1}\). Define
\[
 \begin{split}
 f_N(w,Y)&=N\operatorname{CT}_X
       [U_N(w,X)d_N(X)(1+X^{-N})C_{1,N}(X,Y)],\\
 {\cal D}_{\mu,N}(w,Y,Z)&=
       f_N(w,Y)d_N(Y)Y^{-\mu N}C_{0,N}(Y,Z),\qquad \mu=0,1 .
 \end{split}
 \tag{3}
\]
The third type is three, so there is no outgoing halfweight.

Use the original phases \(Q_\epsilon\) and \(\Psi\), and the
same affine rate as in the core-pair theorem:
\[
 \begin{split}
 F_{123}&=\Psi(e,z_1)+Q_1(s_2;z_1,z_2)
             +Q_0(s_3;z_2,z_3)-g(z_1)-g(z_2),\\
 \Lambda_{123}(z)&=\Re F_{123,*}
   +\Re\{[g'(s_3^*+r_3)-g'(r_3)](z-r_3)\},\\
 \delta&=\min\{(9/20-\Re r_2)^2/250000000,10^{-6}\}>0.
 \end{split}
 \tag{4}
\]
Every star belongs to the same unchanged reference.

**Theorem.** There is a fixed ordinary-color disk about \(-2\)
on which, uniformly for
\[
        Y=e^{-2\pi iq},\quad 1/2\le q\le18/25,\qquad
        Z=e^{-2\pi iz}\text{ as in (1)},
\]
both second Fourier choices and both level parities satisfy
\[
 |{\cal D}_{\mu,N}(w,Y,Z)|
      \le C N^A e^{N\{\Lambda_{123}(z)-\delta/128\}}.
 \tag{5}
\]
Fixed ordinary-color derivatives obey the same rate on smaller
disks. The first sum in (3) is complete. This theorem concerns
the stated second-coordinate interval only.

## 2. Keep the whole cap comparison

At first input \(a=1/2\), let \({\cal A}(0)\) be the maximum
of all six cap comparison rates in
[complete real cap transport](research_mixed_initial44_complete_real_cap_transport.md):
the main line at height \(h_e\), two real cuts, two sampling
corrections with their penalties, and the separate true-end
constant. We do not replace this maximum by its main term.

That theorem bounds the full cap on \(1/2\le a\le7/8\) by
\[
 |U_N(w,e^{-2\pi ia})|
 \le C_\tau N^{A_\tau}
       e^{N\{\max({\cal A}(0),9/10)+\tau\}},
 \qquad w\in[-2,2].
 \tag{6}
\]
Its main profile \(A_0(0)\) is greater than \(181/200\), by
the cap trial traced in Section 3 of
[the far-real-first theorem](research_mixed_443_far_real_first_arc.md).
Since \({\cal A}(0)\ge A_0(0)>9/10\), (6) has rate
\({\cal A}(0)\). This use of the main profile removes only
the additional constant \(9/10\).

Write
\[
 M_2=\max_{1/8\le t\le r_0}
                  \Re Q_1(t+ih_2;1/2,1/2),\qquad
 L(q)=E_{1/2}(1/8;q),
 \tag{7}
\]
where \(r_0<1/2\) is fixed sufficiently close to one half.
Let \(R(q,z)\) be the complete third-factor envelope described
in Sections 3 and 7 of the core-pair theorem. Its entries are
the main, lower and upper horizontal rates on the original
moving interval, with the respective sampling penalties,
and the original half-face third left, half and last comparison
rates. Its proof gives
\[
 |C_{0,N}(e^{-2\pi iq},Z)|
       \le C_\tau N^{A_\tau}e^{N\{R(q,z)+\tau\}}.
 \tag{8}
\]
The joins, wall collar and all physical rows are included in (8).

The half-face comparison in Section 2 of that source is
profilewise. It bounds every cap alternative paired with
every first main or left-cut alternative and every third
alternative, with raw margin greater than \(20\delta\).
Consequently it supplies
\[
 {\cal A}(0)+M_2+R(1/2,z)
                \le\Lambda_{123}(z)-20\delta.
 \tag{9}
\]
Section 3 transports the first real-left rate jointly with
each third horizontal maximum. The other third alternatives
are nonincreasing or constant. The same initial margin gives
\[
 {\cal A}(0)+L(q)+R(q,z)
                \le\Lambda_{123}(z)-20\delta.
 \tag{10}
\]
These inequalities use the explicit comparison functions before
finite summation. They do not infer separate bounds from the
modulus of a cancelling product.

## 3. Refer the critical action to the same half face

Let \(\Theta(a,q)\) be the original zero-lift critical action
from the
[logarithmic branch theorem](research_mixed_real_unit_pair_zero_lift_branch.md).
The [paired action comparison](research_mixed_real_unit_pair_paired_action_transport.md)
gives, entry by entry in the third envelope,
\[
 \Re\Theta(a,q)+R(q,z)
       \le\Re\Theta(a,1/2)+R(1/2,z).
 \tag{11}
\]
For its three horizontal entries this is the paired derivative
inequality. For the remaining nonincreasing or constant entries
it uses the separate decrease of \(\Re\Theta\) in \(q\).
Taking a maximum preserves (11).

Only at \(q=1/2\) do we now use the incoming action comparison:
\[
                 \Re\Theta(a,1/2)\le\Re\Theta(1/2,1/2).
 \tag{12}
\]
Here is why the boundary value is licensed. The
[unit multiplier theorem](research_mixed_four_conditional_unit_multiplier.md)
proves
\[
 \partial_a\Re\Theta=\log\left|\frac{v-X}{1-X}\right|<0
\]
when the outgoing coordinate is on the lower unit semicircle.
For each \(a\in[1/2,7/8]\), the new zero-lift branch at
\(q=1/2\) is simple and has strict strip margins. Its implicit
continuation to \(q<1/2\) is an upper root on the original
zero lift, and hence is that theorem's unique upper root.
Taking the boundary limit gives a nonpositive derivative at
\(q=1/2\). Integrating in \(a\) proves (12). No such sign is
assumed at \(q>1/2\).

To compare the final value in (12) with (7), write its critical
point as \(t_*+i\eta_*\), with \(\rho=e^{2\pi\eta_*}\in(1/2,1)\).
The radius bound follows from the imaginary critical equation,
as in the complete finite-source theorem. At \(a=q=1/2\),
\[
                              t_*>1/8.
 \tag{13}
\]
Indeed, if \(t_*\le1/8\), both squared numerator moduli exceed
\(1+\rho^2>5/4\). The squared own modulus is at most
\[
             (1-\rho)^2+(2-\sqrt2)\rho<3/5.
 \]
The last bound follows by convexity on \([1/2,1]\), using
\(\sqrt2>7/5\) at its two endpoints. These inequalities
contradict the squared critical equation
\(A B=D_s^6\), since \(25/16>(3/5)^3\).
Also \(t_*<1/2\), so choose the common \(r_0\) to contain it.

At this fixed real index, \(\Re Q_1(t_*+i\eta;1/2,1/2)\)
is strictly convex in \(\eta\) at all finite heights, by the
cotangent signs in the zero-lift theorem. Its height derivative
vanishes at \(\eta_*\). Thus
\[
 \Re\Theta(1/2,1/2)
    \le\Re Q_1(t_*+ih_2;1/2,1/2)\le M_2.
 \tag{14}
\]
Combining (9), (11)--(14) proves
\[
 {\cal A}(0)+\Re\Theta(a,q)+R(q,z)
                   \le\Lambda_{123}(z)-20\delta.
 \tag{15}
\]
This comparison retains the whole cap envelope.

## 4. The formerly missing real first interval

The [complete conditional theorem](research_mixed_real_unit_pair_complete_finite_source.md)
now applies to every \(1/2\le a\le7/8\), \(1/2\le q\le18/25\):
\[
 |C_{1,N}(e^{-2\pi ia},e^{-2\pi iq})|
 \le C_\tau N^{A_\tau}
       e^{N\{\max(\Re\Theta(a,q),L(q))+\tau\}}.
 \tag{16}
\]
It estimates all physical rows and all terms in the exact
finite contour formula. This is the step that permits using
the action comparison in a bound for the original polynomial.

The full original Fourier polynomials have rate zero on these
real compact arcs:
\[
 |d_N(e^{-2\pi ia})|+|d_N(e^{-2\pi iq})|
       \le C_\tau N^{A_\tau}e^{N\tau}.
 \tag{17}
\]
This is the absolute bound in
[Fourier-weight continuation](research_mixed_fourier_weight_continuation.md),
since \(J(a),J(q)\ge0\). Both Fourier monomials have modulus
one. Multiplying (6), (8), (16) and (17), then applying
(10) and (15), bounds the complete product
\[
 U_N(w,X)d_N(X)X^{-\nu N}C_{1,N}(X,Y)
                    d_N(Y)Y^{-\mu N}C_{0,N}(Y,Z)
 \tag{18}
\]
at rate \(\Lambda_{123}-20\delta\), before arbitrarily small
source tolerances.

The bound holds for every real ordinary color. Its exact degree
in that color is less than \(N\), so the
[polynomial continuation argument](research_mixed_horizontal_complex_extension.md)
extends it to a sufficiently small fixed disk about \(-2\)
with arbitrarily small rate cost. The other factors are
color-independent multipliers; none is divided out.
Choose all tolerances with total less than \(\delta\).
In particular (18) has gap \(\delta\) on the whole real
first interval in this section. Cauchy's formula gives fixed
ordinary-color derivatives on smaller disks.

## 5. Closing the whole first period

For the two first Fourier terms use the paths
\[
 \Gamma_\nu:\quad
 0\longrightarrow1/10\longrightarrow1/10+ih_\nu
 \longrightarrow11/50+ih_\nu
 \longrightarrow1/2+ih_\nu\longrightarrow1/2
 \longrightarrow7/8\longrightarrow1,
 \qquad h_0=c_1,\quad h_1=H.
 \tag{19}
\]
Every piece now has a bound for the complete product (18):

| First-coordinate piece | Bound used |
|---|---|
| Real \(0\) to \(1/10\), either sector | Positive first-left connection, including the closed endpoint |
| Positive left join and positive horizontal up to \(11/50+iH\) | Positive first-left connection, gap \(\delta/32\) |
| Negative left join and negative horizontal up to \(11/50+ic_1\) | Negative first-left connection, gap \(\delta/64\) |
| Both central horizontals and their right height connections | Complete core-pair theorem, gap \(\delta/4\) |
| Real \(1/2\) to \(7/8\) | Section 4 above, gap \(\delta\) |
| Real \(7/8\) to \(1\), including the endpoint | Far-real-first theorem, gap \(1/200\) |

The [positive connection](research_mixed_443_positive_first_left_connection.md),
[negative connection](research_mixed_443_negative_first_left_connection.md),
core-pair and far-real-first theorems all use the same original
action (4), both second Fourier choices, and both parities.
Their finitely many color disks have a common smaller disk.
Thus every path in (19) has a common gap at least \(\delta/64\),
after fixing the tolerances in Section 4.

For completeness the coefficient normalization is exact.
As a Laurent polynomial in \(X\),
\[
 P(X)=U_N(w,X)d_N(X)C_{1,N}(X,Y)
\]
has support in \([-N+1,2N-2]\). Summing over \(X=\zeta^k\)
therefore extracts only the exponents zero and \(N\):
\[
 \sum_{k=0}^{N-1}P(\zeta^k)
       =N\operatorname{CT}_X[(1+X^{-N})P(X)]
       =f_N(w,Y).
 \tag{20}
\]
On the physical nodes this is precisely
\(\sum_k U_N(w,\zeta^k)C_{1,N}(\zeta^k,Y)/P_k\).

For each \(\nu\), \(P(e^{-2\pi ia})e^{2\pi i\nu Na}\)
is entire and one-periodic in \(a\). Its integral on
\(\Gamma_\nu\) equals its integral on \([0,1]\), namely
\(\operatorname{CT}_X[X^{-\nu N}P(X)]\).
Multiplying by the original density \(N\) and adding the two
sectors gives (3), with no changed root-average convention.
The remaining factors in (18) are independent of \(a\).
The path lengths, densities and finite number of pieces cost
only a polynomial. Keeping the weaker gap \(\delta/128\)
proves (5).

The result completes the first sum on this real second interval.
It does not complete the second period, give a nonzero coefficient
after that next integration, or establish finite exceptions
for arbitrary short fillings. Those remain further obligations.

## Direct source versions

| Direct source | SHA-256 |
|---|---|
| research_mixed_443_core_first_complete_right_pair.md | 3f3fa659048dd5961e54a29d71bdcd6e6b73bd4927e4d802ffa8e0849b86cd21 |
| research_mixed_initial44_complete_real_cap_transport.md | dd8d313e1e23240943421b6fbb340f28de769f46d2c0f98f3a4a749be20d4420 |
| research_mixed_443_far_real_first_arc.md | 21170ee7d4fbeb0c01e7fe440d31a3f356480b68c249f51efa1bd68bc068e6c3 |
| research_mixed_real_unit_pair_zero_lift_branch.md | 4e22a14247e7b11340d9b9ade4774760cd93722f82feb16c12ff2faa1c2b4d1a |
| research_mixed_real_unit_pair_paired_action_transport.md | 7b233b397d084a0c5bbcc40ddc1df7bd65b7917d85c7e68581e90856fb03a8e8 |
| research_mixed_four_conditional_unit_multiplier.md | 4d73d90557948056413ef0445cb7754569cbbc03e7ff3f35ecab0f3e9fe8f66f |
| research_mixed_real_unit_pair_complete_finite_source.md | 08d0d47f6663eefe6162f4f3b73986bbbba9a25fb862bfd8b78a5c6d7ddae9a8 |
| research_mixed_fourier_weight_continuation.md | 0bae41d83f414eb91fd137de1242120a11408147d56ec752e466ca5ed7e7f48e |
| research_mixed_horizontal_complex_extension.md | c7837a9dfb072f2e276f5ccdb99c7421e154a4ca073a078540d8064dbb3747d4 |
| research_mixed_443_positive_first_left_connection.md | 722735ec78c9db665073a35008e5b5af3f47583fe582f85eb8f2a0fb8063d32b |
| research_mixed_443_negative_first_left_connection.md | 74616de714ca8ab6f2059129b3aaf0ee38cc82f676317d20d3c22e4ec7512d94 |

Written mathematics only. No mathematical numerical evaluation,
test, import, compilation or change to a frozen source is used.
The root author read the entire final proof and all eleven directly
used source implications, including the raw six-profile cap
calibration and the full finite contour bounds. All eleven source
hashes match. Separate full proof and direct-source review is
required before adoption.
