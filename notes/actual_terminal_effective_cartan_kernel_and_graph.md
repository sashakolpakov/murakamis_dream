# The effective terminal Cartan coupon: an exact kernel and its two critical channels

29 October 2026. This continues the [literal terminal Ward
calculation](actual_terminal_phase_coupon_and_ward.md). The complete
Steinberg projection can be expanded before taking a classical symbol.
Its kernel has an exact root-orbit completion. There are consequently
two coherent channels, rather than just the phase-one Hurwitz graph.
The regular graph of the first channel is explicit below. The second
has an explicit coefficient integral and saddle equations. Neither
channel is independently substituted for the original source.

This note does **not** prove a full selected-cycle energy bound, or a
closed-knot stationary counterexample. In particular its last section
keeps the normal equation of the outgoing cap: the finite character
cap is at an escaping physical Fourier coordinate. A character
intersection alone does not settle that normal equation.

## 1. Exact completion on every original input

Use (N\geq2,d=N-1,q=e^{\pi i/N},Q=q^2,x=q^d), and

\[
 F_a=(Q;Q)_a,\qquad L=\kappa^{-1}R_{12}|_W,
 \qquad W=(V\otimes V)_{\deg d}.
\]

The lowest lift and effective coupon, with all normal coefficients, are

\[
 D w=\sum_{k=0}^d\frac{F_{12}^{\,k}}{F_k}Lw\otimes|d-k\rangle,
 \qquad
 M_t=\xi_d^{-1}R_{\rm high}E_{123}^{,d}t^{J_2}D,
 \quad \xi_d=(-1)^dN.                                      \tag{1}
\]

They are the original maps, including the full common Cartan factor in

\(R\); in particular (M_1=I). A useful ALL-INPUT identity is

\[
 \boxed{\quad M_t=\mathcal N_t L,\qquad
 \mathcal N_t=\left.
 \sum_{k=0}^d
 \frac{x^kQ^{k(k+1)/2}}{F_k^2}
 E_{12}^{,k}t^{J_2}F_{12}^{,k}\right|_W .\quad}             \tag{2}
\]

Here (t^{J_2}|a,b\rangle=t^b|a,b\rangle). No inverse of the
terminal packet is used. To prove (2), put

\[
 A=E_{12}K_3,\quad B=E_3,\quad AB=QBA.
\]

In ((A+B)^d=\sum_k{d\brack k}_Q B^{d-k}A^k), only the term
with (k) pair arrows sends the last color (d-k) to zero. Its
coefficient, after (1), is

\[
 \frac{{d\brack k}_Q x^kQ^{-k(d-k)}
 Q^{-(d-k)(d-k+1)/2}F_{d-k}}{F_k\xi_d}
 =\frac{x^kQ^{k(k+1)/2}}{F_k^2}.
\]

Notice the sign: \(\prod_{a=1}^r(Q^{-a}-1)
=Q^{-r(r+1)/2}F_r\). Thus (2) also proves the exact inverse identity

\[
 \mathcal N_1=L^{-1}.                                    \tag{3}
\]

It retains the complete total-character projection, not only its
Casimir value or a formal fixed-moment constraint.

## 2. A factorized open kernel, including its orbital alias

Let (i,j=0,\ldots,d) be the output and input indices of
\(\mathcal N_t\), and define

\[
 \mathcal R_{ij}=\sum_{a=\max(i,j)}^d
       \frac{F_a^2}{F_{a-i}F_{a-j}},
\]
\[
 \mathcal S_{ij}(t)=
 \sum_{s=\max(0,j-i)}^j
 (tQ^{i+j-d})^s
 \frac{F_{d-j+s}^2}{F_sF_{s+i-j}}.
\]

Then the exact finite kernel is

\[
 \boxed{\quad
 (\mathcal N_t)_{ij}=
 \frac{x^{j-i}Q^{i(i-j)}t^{d-j}}
      {F_jF_{d-j}F_iF_{d-i}}
       \mathcal R_{ij}\mathcal S_{ij}(t).\quad}             \tag{4}
\]

For an elementary derivation, let (r,s) be the first- and
second-head raising counts in (F_{12}^{r+s}). The lowering counts
in (E_{12}^{r+s}) are (u=j+r-i) and (v=s+i-j). Their factorial
denominators are (F_rF_sF_uF_v). Multiplication in (2) leaves

\[
 x^{j+2r-i}Q^{-dr-ds+i^2-ij+is+js}t^{d-j+s}
 \frac{F_{j+r}^2F_{d-j+s}^2}
 {F_jF_{d-j}F_iF_{d-i}F_rF_sF_uF_v}.
\]

Since (x^2=Q^d), its (r) phase cancels exactly. The allowed

\(r\) and (s) ranges are independent rectangles. This proves (4).

The first factor has the exact orbit evaluation

\[
 \boxed{\quad
 \mathcal R_{ij}=N\left(1+
 [z^N](Q^{1-i}z;Q)_i(Q^{1-j}z;Q)_j\right).\quad}           \tag{5}
\]

Indeed the summand is

\((Q^{a-i+1};Q)_i(Q^{a-j+1};Q)_j\). Extend its (a)-sum to a
full (N)-orbit: the additional terms vanish. The polynomial has
constant coefficient one and degree (i+j<2N), so only its constant
and (N)-th coefficients survive that orbit. In particular

\[
 i+j<N\quad\Longrightarrow\quad\mathcal R_{ij}=N.          \tag{6}
\]

The second coefficient in (5) is not deleted outside this triangle.
Nor may one find saddles of the unsummed \\(a\)-sum and regard all
of them as separate contributions: (5) already cancels all its
nonconstant modes in (6).

## 3. The regular constant-channel canonical graph

Here is a precise principal-phase calculation for the constant channel
of (5). It applies where all indicated shapes are regular and the
\(s\)-sum has an interior saddle. It describes that critical
correspondence; it does not assert that this saddle meets the selected
source cycle.

Write (h=\log Q), (I=e^{hi},J=e^{hj},S=e^{hs}), and set

\[
 B=S/J,\qquad V=SI/J.
\]

The exact adjacent summand ratio in \(s\) tends to one precisely when

\[
 tIJ(1-S/J)^2=(1-S)(1-SI/J).                             \tag{7}
\]

Input and output canonical momenta of (4), after taking the constant
\(N\) channel, are

\[
 z_{\rm in}=(1-S)/S,\qquad
 z_{\rm out}=\frac{SI/J}{1-SI/J}.                         \tag{8}
\]

These follow by the exact \(j\) and \(i\) ratios, respectively;
input momentum is the inverse input ratio. Solving (7)--(8) gives

\[
 z_{\rm out}=\frac{z_{\rm in}}
 {t[J(1+z_{\rm in})-1]^2},\qquad
 I=\frac{J(1+z_{\rm in})z_{\rm out}}{1+z_{\rm out}}.
\]

At (t=1) this is the original graph of (L^{-1}), consistently
with (3). Composing it with (L), the regular constant-channel graph
of the effective coupon itself is therefore

\[
 \boxed{\quad
 (J,z)\longmapsto
 \left(\frac{J(1+z)}{t+z},\frac zt\right).
 \quad}                                                   \tag{9}
\]

It preserves (d\log J\wedge d\log z). The recorded physical
clock is (B=z/[J(1+z)]), invariant under (9).

To express (9) on the ACTUAL character cubic, the symbols of the
literal complete Casimir matrices give

\[
 X=A-2=-\frac{(1-J)^2(1+z)^2}{z},\quad
 Y=B_{\rm Cas}-2=\frac{(J-1)^2(1+z)}J,\quad
 Z=C-2=\frac{(J-1)^2(1+z)}{Jz}.
\]

They satisfy ((X+Y+Z)^2+XYZ=0). In these coordinates (9) is

\[
 \boxed{\quad (X,Y,Z)\longmapsto\lambda(X,Y,tZ),\qquad
 \lambda=\frac{(X+Y+tZ)^2}{t(X+Y+Z)^2},\qquad
 B_{\rm clock}=-Y/X.\quad}                              \tag{10}
\]

This is a nontrivial algebraic canonical action. Parseval matching of
the recorded clocks in its two copies does not algebraically set
\\(t=1\). On the true irreducible terminal \(R_{23}^2\)-cap
component one must impose

\[
 (X',Y',Z')=(c^2,c,-c),
\]

not just its unsaturated equation (Y'+Z'=0). In particular the
condition (Y+tZ=0) alone cannot replace the full cap source.

## 4. The second, coherently retained critical correspondence

Put

\[
 A_{ij}=[z^N](Q^{1-i}z;Q)_i(Q^{1-j}z;Q)_j.
\]

Its exact Cauchy coefficient integral supplies a second phase. At a
regular nonzero coefficient saddle (w), its leading action is

\[
 \Phi=\operatorname{Li}_2(w/I)+\operatorname{Li}_2(w/J)
 -2\operatorname{Li}_2(w)-2\pi i\log w,
\]

with the inherited logarithmic sheets retained. Its stationary
equation is

\[
 (1-w)^2=(1-w/I)(1-w/J),\qquad
 w=\frac{2IJ-I-J}{IJ-1}.                                 \tag{11}
\]

Consequently, with (R=w/J,U=w/I,V=SI/J), the second
correspondence is specified by (7), (11), and

\[
 z_{\rm in}=\frac{1-S}{S(1-R)},\qquad
 z_{\rm out}=\frac{V(1-U)}{1-V},\qquad B_{\rm clock}=S/J.   \tag{12}
\]

One then composes with the SAME original (L). At (t=1), away
from excluded denominators, (7) implies (S=R^{-1}); (12) gives
both momenta \(-1\). Thus this channel degenerates into the
reducible character fiber at phase one. This is consistent with
the exact identity \(M_1=I\); it is not permission to omit the
channel at other phases. Equations (11)--(12) retain precisely the
orbital completion missing from (9).

Endpoint saddles of the finite sums and logarithmic/coordinate
boundary strata still require their own source analysis. This note
does not identify their union with a selected global canonical cycle.

## 5. An exact source/cap intersection and its remaining normal test

The endpoint issue is visible without arbitrary exterior data. Take
the literal one-component four-plat word \([-2,1,2,2]\), so its
prefix is \(B=R_{12}R_{23}^{-1}\). The actual source gives

\[
 R_{23}^{-1}p=N\kappa^{-1}e_d,
 \qquad L Bp=N L^2e_d.
\]

The latter vector has the all-level finite formula

\[
 (L^2e_d)_j=N^2x^{j-d}\frac{F_j}{F_{d-j}}
 \sum_{v=0}^j
 \frac{(-1)^vQ^{v(v+1)/2-jv}}{F_{j-v}F_v^3}.              \tag{13}
\]

Its interior saddle, writing (V_0=e^{hv}), satisfies

\[
 JV_0^2-3JV_0+3J-1=0,\qquad
 z_{\rm source}=\frac{(1-J)^2}{J(V_0-J)}.                 \tag{14}
\]

The source curve before the final \(L\) is exactly
\((X,Y,Z)=(s,s^2,-s)\), by the literal Hurwitz maps. Formula
(14) gives its image under that final \(L\), not an independently
chosen boundary phase.

On the alias correspondence, take the irreducible terminal cap chart
\(I\to\infty\), \(z_{\rm out}=-1+c/I+O(I^{-2})\). Put
\(m=S/J\). Equations (7), (11)--(12) then give

\[
 J=\frac m{m^2-t(1-m)^2},\quad S=mJ,\quad
 c=(t-1)(m+m^{-1}-2).                                    \tag{15}
\]

The incoming effective-coupon character is

\[
 X=\frac{(m-1)^2(t-1)^2}{t},\quad
 Y=\frac{(m-1)^2(t-1)(mt-m-t)^2}{mt},
\]
\[
 Z=-\frac{(m-1)^2(t-1)
 (m^2t^2-2m^2t+m^2-2mt^2+3mt-m+t^2)^2}{mt^2}.            \tag{16}
\]

There are exact nontrivial unit/unit parameters satisfying the actual
prefix curve \(Y=X^2,Z=-X\). For example let \(a\) be the unique
real root in \((131/100,33/25)\) of

\[
 a^6-3a^5-a^4+6a^3-2a^2+14a-19=0,
\]

put \(m=(a+i\sqrt{4-a^2})/2\), and set

\[
 t=\frac1{107}\big(50m^{11}-126m^{10}+181m^9-343m^8
 +267m^7+295m^6-332m^5-88m^4+397m^3-214m^2+69m-24\big).
                                                               \tag{17}
\]

Polynomial reduction proves \(t\bar t=1\), \(t\ne1\), and the
two source equations exactly. Numerically

\[
 m=.658593303580947+.752499076729224i,
 \quad t=.776413057400676-.630224376153235i,
\]
\[
 s=.201092454204344+.229765297192068i,
 \quad c=.152668158870543+.430325644530469i.
\]

Both characters are finite and irreducible, by the
[explicit cap atlas](actual_parabolic_cap_trace_certificate.md). The
two conjugate copies have matching unit recorded clock \(m\). The
actual source saddle (14) is regular at these values. This is an
explicit intersection of the completed critical correspondence, the
actual prefix source curve and the genuine terminal cap component.

**Its normal qualification is essential.** The exact outgoing row is

\[
 (\ell R_{23}^2)_i=(xQ)^{i-d}/N.                         \tag{18}
\]

This follows by the original anti-Pascal matrix and the elementary
identity \(\sum_{v=0}^aQ^v/F_v=1/F_a\). Hence full adjacent
output stationarity requires

\[
 z_{\rm out}=(xQ)^{-1}=-q^{-1}
                =-1+h/2+O(h^2).
\]

Together with the cap chart this permits, and requires at leading
order, \(I\sim2c/h\). It does not give \(c=0\). Proving a
source-preserving full normal critical lift in this N-dependent chart
requires controlling the same retained norm/logarithmic sectors;
it is not a consequence of the reduced character equations (15)--(17).
No such lifting or selected intersection number is asserted here.
Accordingly this example is not advertised as a full stationary
counterexample or as a nonzero contribution to the quantum period.

The actionable calculation is (2)--(5), followed by the two different
critical relations (9) and (11)--(12). A proposed geometric estimate
of the terminal Parseval energy must handle their coherent completion
and the cap normal equation (18). Clock matching alone is insufficient
to replace that calculation by a transparent original-knot seam.

## 6. What conjugate Parseval matching says on the first channel

The doubled stationary equation must keep the opposite-root convention.
If \(m_+\) is the recorded clock in the first copy and \(\bar m_-\)
the clock in the conjugate-root copy, differentiation in the retained
phase gives

\[
 \log m_++\log\bar m_-=0
\]

on the inherited sheets (equivalently equality of the two integer
recorded colors before taking a symbol). On a conjugation-fixed real
critical stratum this implies \(|m|=1\). A real retained phase also
has \(|t|=1\). It does not say that every complex stationary point
of a deformed doubled period lies in that stratum.

For the first correspondence, the irreducible terminal cap condition
in (10) is \(t=-Y/Z\), with its full component retained. Therefore
its conjugation-fixed stationary characters satisfy

\[
 |X|=|Y|=|Z|,\qquad m=-Y/X,\qquad t=-Y/Z.                 \tag{19}
\]

This is a concrete condition on the incoming prefix character curve.
It is weaker than \(t=1\). Conversely, if \(m,t\) are unit numbers
and the denominators are nonzero, the cubic and terminal cap determine

\[
 X=\frac{t(1-m+m/t)^2}{m^2},\qquad
 Y=-mX,\qquad Z=mX/t.
\]

The outgoing cap parameter is \(c=-1/m\). Thus this first channel
has a particularly explicit angular locus; the alias channel (15)
has a different relation between recorded clock and cap parameter.
They cannot be conflated in a doubled-energy estimate.

As a check with the literal figure-eight prefix
\(R_{12}^{-1}R_{23}\), its transported source curve is

\[
 (X,Y,Z)=(s,s^2,-s(1+s)^2).
\]

Substituting in (19) gives \(|s|=|1+s|=1\), hence
\(s=e^{\pm2\pi i/3}\) and \(t=s/(1+s)^2=1\). This is an
algebraic transparency check for that channel and that actual prefix.
It does not control the alias, escaping cap normal, or non-real doubled
critical strata. It is therefore not a substitute for the exact
figure-eight packet proof or a broad knot-energy theorem.

## 7. Shrinking the phase does not bound all character ratios

The condition |m|=1 above comes from stationary matching in the phase
variable. An endpoint of a restricted real phase arc does not supply
that equation. Bounded actual character coordinates do not replace it,
since m is a ratio.

There is an exact escape in (15)--(16), using the SAME original prefix
and cap as Section 5. Put tau=t-1 and write m=1+w/tau. The actual source
equations Y=X^2 and Z=-X are satisfied exactly whenever

    w^3-w^2+2tw-t=0.                                      (20)

This follows by direct substitution in their common factor, not by
choosing independent exterior data. At t=1 the polynomial has
discriminant -23, so all three roots are simple and nonzero. Each has
a local analytic continuation w(t), including along t=exp(i theta)
as theta tends to zero. The real root at one lies in (0.56,0.58).

Along each branch the incoming character and outgoing cap parameter are

    (X,Y,Z)=(w^2/t,w^4/t^2,-w^2/t),
    c=w^2/(w+tau).                                        (21)

They remain bounded and tend to finite irreducible characters. In
particular the incoming limit has X=w(1)^2 != 0. Nevertheless
|m| is comparable to |t-1|^(-1). The fixed-t cap normal calculation
suggests I comparable to 2w(1)/h, a polynomial-radius physical chart.
Its uniform validity when |t-1| is smaller than |h| is a separate
joint-limit question; the fixed-t expansion does not prove it.
Thus t near one and bounded character coordinates alone do not
exclude the reduced channel, but do not prove its full normal lift.

With v=w(1), the limiting incoming coordinates may equivalently be
written (v^2,v(v-1)^2,-v(v^2-v+1)^2). Equation (20) makes this exactly
(v^2,v^4,-v^2). This also checks the unscaled limit of (16), including
its genuine cap component.

This is an algebraic escape certificate, not a proof that an extra
contribution survives in the original quantum arc integral. The
normal sectors may still cancel this channel, as the exact identity
M_1=I requires at phase one. Its calibrated action and coefficient
must be retained to decide suppression for |t-1|=N^(-A). Polynomiality
alone does not assign that action or its selected intersection number.
No shrinking-arc sharp-energy theorem is claimed here.

There is a useful action test before asserting suppression. On any
genuinely stationary branch with the original t-dependence retained,
the envelope identity gives

    d S / d log(t) = log(m),

with the inherited integer color lift. All original scalar factors
are t-independent; the identity follows directly from t^n in (1).
For m=1+w/tau with w tending to a nonzero limit, it gives on a fixed
logarithmic sector

    S(t)=S_* - tau log(tau) + O(tau).                       (22)

An additional bounded 2pi*i color lift changes only the O(tau) term.
Hence this phase differential does not itself yield a positive
N*log|tau| vanishing factor. It also does not calculate S_*, prove
that the branch is stationary in every retained normal variable,
or determine its selected coefficient. Those are essential to any
actual suppression or survival claim. The exact cancellation at t=1
must not be replaced by assigning an unproved value to S_*.

## 8. Finite diagnostics of the actual first phase jet

The [saved diagnostic](../experiments/diagnose_terminal_cartan_jet_and_arc.py)
uses the exact closed T kernel and (13), with the original prefix
B=R12 R23^-1. It forms the literal coefficient vector f_n=T_n(Bp),
the value sum f_n, and the first phase jet sum n*f_n. It also evaluates
the normalized shrinking-arc energy EXACTLY as the finite moment sum

    E_a=sum_(n,m) f_n conjugate(f_m) sinc(a(n-m)), a=N^-3.

All quantities use two working precisions; the saved values agree
to at least 24 relative decimal places. Some measured rates are

| N | log of first-jet modulus / N | log(E_a)/(2N) |
|---|---:|---:|
| 16 | 0.651957431682358 | 0.259217703955373 |
| 32 | 0.582429288600779 | 0.240456892692090 |
| 64 | 0.532365673879463 | 0.328835120972563 |

These are finite diagnostics. They do not prove a positive limiting
jet rate, identify the jet with another knot invariant, or prove
that the escaping critical branch supplies its asymptotics. They
show why the proved shrinking-arc Cauchy inequality must be accompanied
by a quantitative estimate of the actual normal jets; continuity at
phase one alone is inadequate for that estimate.

[Audit](../experiments/audit_actual_terminal_effective_cartan_kernel.py)
compares (2), (4), (5), (13), and (18) with the original full physical
maps. It also checks the rational symplectic/cubic calculations and
the exact unit/unit algebra in (17). No selected-cycle test is hidden
in those algebraic checks.
