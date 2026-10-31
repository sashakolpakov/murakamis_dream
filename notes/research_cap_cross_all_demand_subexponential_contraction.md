# The original cap/CROSS signed contraction at every demand and both parities

31 October 2026. Internally reviewed analytical theorem. Root and coherent completed
full independent analytical/source reviews, including the actual
coefficient lower estimates and both finite cutoff currents. This is
not external peer review. No nearby-spectrum or whole
source/filling assertion is made.

## 1. Exact statement and comparison source

Keep the original overlapping pair \(E=(A,0,C,Z)\), \(F=(0,A,0,C)\),
with A internal to these ports and its unchanged demand \(A^d\),
\(d=N-1\). Put raw E at \(-2\), raw F at \(+2\), and retain E's
CROSS and F's RIGHT parts. Write
\[
 M=\lfloor N/2\rfloor-1,\qquad H=\lfloor d/2\rfloor,
 \qquad J_n=\{\max(0,n-H),\ldots,\min(M,n)\}.
\]
Then \(M+H=N-2\), and the original signed coefficient, apart from its
common raw sign \((-1)^d\), is
\[
 T_{N,n}=\sum_{j\in J_n}(-1)^jU_j C_{j,n-j},
                   \qquad0\le n\le N-2.              \tag{1}
\]
All original unused factors, source turns, and remaining exponents
\(C^nZ^{d-n}\) are retained.


For explicit normalization, put \(\theta=\pi/N\),
\[
 c_r=2\cos((2r+1)\theta),\quad a_r=2+c_r,\quad
 \gamma_r=2-c_r,\quad s_r=2\sin(r\theta),\quad
 B_j=\prod_{r=1}^j s_r^2,\quad B_0=1,
 \qquad U_j=\frac{4B_j}{\prod_{r=0}^j\gamma_r}.
\]
The original continuant and unused suffix are
\[
\begin{aligned}
 K_0&=1,\qquad K_1=s_1^2(A+Z),\\
 K_r&=s_r^2(A+Z)K_{r-1}
           +s_rs_{r-1}a_{r-1}AZK_{r-2},\\
 C_{j,h}&=[A^jZ^{d-h-j}]K_{d-h}(A,Z)
                              \prod_{r=d-h+1}^{d}a_r.
\end{aligned}
\]
Set C to zero outside \(0\le h\le d,0\le j\le d-h\).
These are the full literal coefficients from
[the original-demand source](research_two_port_main_cap_original_demand_convolution.md),
sections 1–2, extended before applying the cutoffs in (1).
At odd levels \(a_{(N-1)/2}=0\) is retained, never divided out.

At even N the positive comparator is
\(D_{N,n}=\sum_{j\in J_n}V_jC_{j,n-j}\).
At odd N it is
\(D_{N,n}^o=\sum_{j\in J_n}V_j^o\overline C_{j,n-j}\),
from the actual fixed-root regularizer
\(V_N(-2)-N^{-2}\partial_\sigma V_N(-2)\) at both ports.
Explicitly, on the original cap range,
\[
 V_j=\frac{4B_j}{\prod_{r=0}^j a_r}\quad(N\text{ even}),
 \qquad V_j^o=\frac{B_j}{\prod_{r=0}^j a_r}\quad(N\text{ odd}).
\]
The odd denominators contain no central zero. The actual coefficient
\(\overline C_{j,h}\) is obtained from the CROSS part of
\(H_{F_N}(A,0,C,Z)\), with the spectral derivative at the fixed root;
its original normalization and positivity are proved in
[odd regularization](actual_fejer_odd_regularized_full_numerator.md), sections 1–3.
Let \(D_{N,n}^{\mathrm{ref}}\) denote the appropriate one. These
are positive for every nonempty range in (1).

**All-parity theorem.**
\[
 \boxed{\limsup_{N\to\infty}
   \frac1N\log\max_{0\le n\le N-2}
            \frac{|T_{N,n}|}{D_{N,n}^{\mathrm{ref}}}
                        \le0.}                       \tag{2}
\]
This is a subexponential bound, not a claimed polynomial factor.
The raw numerator is never replaced by its regularized reference.

The reviewed [even](research_cap_cross_full_low_demand_subexponential_contraction.md)
and [odd](research_cap_cross_odd_low_demand_subexponential_extension.md)
full-low theorems prove (2) for \(n\le M\) at both
parities. The [reviewed high-demand theorem](research_cap_cross_high_demand_signed_contraction.md),
sections 1–7, proves it with explicit
polynomial factors for
\(n\ge n_H:=\lceil3N/4-3/2\rceil\).
[The all-odd middle proof](research_cap_cross_all_odd_demand_subexponential_contraction.md)
has separately closed every missing odd index. It remains to prove
the even middle, without identifying it with an auxiliary full slice.

## 2. A genuine all-parity contiguity and both cutoff currents

Use the [original Newton source dictionary](research_cap_cross_low_demand_newton_contraction.md),
sections 2–3, with
\[
 \widehat B_j(z)=B_j^{-1}\prod_{r=0}^{j-1}(c_r-z),
 \qquad Z_Ne_j=c_je_j-s_{j+1}^2e_{j+1}
\]
(the last off-diagonal term is zero). Its physical turn identity
retains all repeated nodes and all original cup/mark factors.
Use the nonnegative row
\[
 v_j=B_j\prod_{r=j+1}^d a_r,\qquad B_j=\prod_{r=1}^j s_r^2 .
\]
The physical three-port adapter with the monomial coupon
\(\widehat B_j\) gives exactly
\[
 C_{j,h}=v^T\widehat B_j(Z_N)e_{d-n},\qquad n=j+h.
                                                               \tag{3}
\]
This is the same literal source identity used to derive the full
recurrence; the cap specialization of \(\widehat B_j\) is
\(A^{d-j}C^j\). It holds before any truncation.

The Newton relation
\((c_j-Z)\widehat B_j=s_{j+1}^2\widehat B_{j+1}\), and
\(Z_Ne_k=c_ke_k-s_{k+1}^2e_{k+1}\), yield
\[
 s_{j+1}^2 C_{j+1,h-1}
       =(c_j-c_n)C_{j,h}+s_n^2 C_{j,h-1}.              \tag{4}
\]
Reflection \(c_{d-n}=c_n\), \(s_{d-n+1}=s_n\) is exact.
Set \(t_j(n)=(-1)^jU_jC_{j,n-j}\).
Using \(\gamma_{j+1}U_{j+1}=s_{j+1}^2U_j\), equation (4) becomes
\[
 \gamma_n t_j(n)+s_n^2t_j(n-1)
       =\gamma_jt_j(n)-\gamma_{j+1}t_{j+1}(n).         \tag{5}
\]

For the middle indices \(n>H\), put \(L=n-H\), so
\(J_n=[L,M]\) and \(J_{n-1}=[L-1,M]\).
Sum (5) over the ORIGINAL range, then use (5) at \(j=L-1\)
for the adjacent-projector difference. This proves
\[
 \boxed{\gamma_nT_{N,n}+s_n^2T_{N,n-1}
   =(\gamma_{L-1}-\gamma_n)t_{L-1}(n)
                     -\gamma_{M+1}t_{M+1}(n).}        \tag{6}
\]
Both boundary currents are explicit. No top coefficient or lower
projector has been omitted.

At odd \(N=2m+1\), the first coefficient has \(h=m+1\) and
vanishes by the actual unused central zero. Equation (6) reduces
to the already reviewed odd flux. Its one transition index \(n=m=H\)
was separately retained in that proof.

At even \(N=2m\), \(H=M=m-1\), the two actual boundary coefficients
are
\[
             C_{n-m,m},\qquad C_{m,n-m}.               \tag{7}
\]
The first is a genuine one-sided boundary term just beyond the
finite CROSS cutoff, not a CROSS coefficient silently inserted in it.

## 3. The actual even comparator has the same uniform rate J

Put \(u=n/d\), \(t=u-1/2\), and
\(f(t)=-\int_0^t\log\tan(\pi s)\,ds\).
The comparator rate obtained in the odd proof is
\[
 J(u)=f(t)+\max_{t\le a\le1/2}
                         [3f(a)+f(a-t)].              \tag{8}
\]
It is strictly concave and has a unique peak \(u_*\in(1/2,3/4)\).
Those conclusions depend only on the displayed continuous entropy,
not on level parity.

Here is the genuine even LOWER input. The
[closed half-block entropy theorem](actual_fejer_half_block_entropy.md)
section 5, equation (15), proves coefficientwise
\[
 B_{\mathrm{cross}}
     =4(A+Z)\mathcal D(A,0,Z)\mathcal D(A,C,Z)
       \le P_{\mathrm{cross}}<3B_{\mathrm{cross}},       \tag{9}
\]
where \(\mathcal D(A,b,Z)=R_M^*(b)\) is exactly the modified
lower-block path numerator of its equation (15).
If one instead uses its determinant denoted \(D_M\), then
\(\mathcal D=C_{\mathrm{front}}D_M\) with
\(C_{\mathrm{front}}=N/[2\sin(\pi/N)]\). This scalar is retained
in (9), not dropped from the exact inequality.
The same theorem proves uniform CLOSED triangle coefficient upper
and lower rates for these \(\mathcal D\)'s. Their total degree is M,
so \(M/d=1/2-1/(2d)\); this shift vanishes uniformly by closed
continuity. The forced outer factor in (9) must remain.

In the actual \(j=M\) comparator term choose the forced outer Z.
Then the genuine latent A-degree k has integer interval
\[
                   n-M\le k\le M .                   \tag{10}
\]
On the middle interval the limiting maximizing a in (8) is interior;
rounding it into (10) costs \(O(1/d)\). Thus the forced Z term in
the exact positive block supplies a matching lower rate. This is
not an inference from a weighted capacity or an upper-only theorem.

For the upper estimate, all latent allocations have, up to \(O(1/d)\),
the same objective as in the odd calculation:
\[
 2f(a)+f(v-a)+f(u-v)+f(u-a)-2f(v),
                  \qquad t\le a\le v\le1/2.
                                                               \tag{11}
\]
Here \(v=j/d\), and the actual even cap product gives
\(N^{-1}\log V_j=-2f(v)+o(1)\) uniformly.
Its derivative in v is positive, so the maximum is \(v=1/2\)
and equals (8). The polynomial number of positive terms, the
two-sided closed theorem, and (10) prove
\[
                N^{-1}\log D_{N,n}=J(n/d)+o(1)         \tag{12}
\]
uniformly for \(M<n\le n_H\), including \(n_H\).
The adjacent starting index n=M has rate \(J(1/2)+o(1)\).
All d-versus-N and forced-unit offsets are absorbed by closed
continuity; no finite support is enlarged for the lower estimate.

## 4. Both even currents lie below that same rate

The cap boundary \(C_{m,n-m}\) in (7) has normalized A-load
\(m/d=1/2+O(1/d)\), C-load \(t+O(1/d)\), and input middle zero.
Its limiting endpoint CROSS entropy is precisely J(u), as in
the odd flux calculation. The original uniform closed coefficient
upper theorem therefore bounds it by
\(\exp\{N[J(u)+o(1)]\}\).

The new lower-cutoff coefficient \(C_{n-m,m}\) approaches the
actual endpoint seam
\[
        (q_x,q_b,q_c,q_y)=(t,0,1/2,1/2-t).
\]
The [uniform original closed upper theorem](research_global_sharp_coefficient_limsup_majorant.md),
section 4, equation (12), at \(\delta=0\), and the
[closed Green/seam formula](research_sharp_green_spectral_maximum.md),
sections 1 and 5, give its rate at most \(2f(t)\).
This statement applies to the actual one-sided finite coefficient;
it does not require a CROSS lower formula for that coefficient.
Since choosing \(a=t\) in (8) gives
\[
                         J(u)\ge4f(t)\ge2f(t),         \tag{13}
\]
this additional current is also bounded at rate J.

All prefactors in (6) are polynomial: the gammas are bounded,
\(U_j\le C N^2\) for \(0\le j\le m\), and the relevant cap indices
are \(j=n-m\) and \(j=m\). The U bound follows directly from its
shifted sine-product formula: it decreases up to \(m-1\), and the
next ratio is bounded, while \(U_0=O(N^2)\).
Consequently the entire right side of (6) has the uniform bound
\[
                     e^{N[J(n/d)+o(1)]}.              \tag{14}
\]

## 5. Two-sided propagation completes the even middle

On all indices from M to \(n_H\), the raw recurrence coefficients
\(s_n^2,\gamma_n\) are bounded away from zero, and
\[
 \left|\log\frac{s_n^2}{\gamma_n}\right|\le C/N .
                                                               \tag{15}
\]
Every forward or backward subinterval product is therefore bounded.
Propagate (6) forward from the reviewed low endpoint n=M up to
the peak of J. Every encountered current has rate at most the
current J because J is increasing there. The initial low estimate
has rate \(J(1/2)\). The O(N) terms and bounded propagators give
\[
                    |T_{N,n}|\le e^{N[J(n/d)+o(1)]}.
\]
For indices beyond the peak, propagate backward from \(n_H\),
where the proved even high-demand estimate is \(|T_{N,n_H}|\le D_{N,n_H}\).
Now J decreases, so every boundary/current rate is again at most
the current J. The same estimate follows. Rounding around the
single peak costs o(1) in rate.

Divide by the actual lower estimate (12). This proves the
subexponential ratio on the even middle, uniformly in n.
Together with the reviewed low/high intervals and the reviewed
odd middle proof, it proves (2).

## Scope

Every degree in the original nonempty J_n has been covered, with
both finite boundary currents retained. The proof asserts neither
a polynomial all-demand factor nor estimates on a spectral
neighborhood. It does not identify independent overlapping
Casimirs, introduce a semisimple coupon adapter, or compare arbitrary
exterior face targets. A whole-source or filling consequence would
require its own assembly argument.

The new ingredients in this draft are the exact general contiguity
(3)--(6), the even forced-unit lower check (9)--(12), and the
seam-current comparison (13)--(14). No numerical growth experiment
is used as proof.


## Internal review and finite source verification

Root and coherent completed full independent analytical/source reviews.
They checked the all-parity Newton contiguity, both actual cutoff currents,
the even forced-Z coefficient LOWER with its retained cofactor scalar,
the odd regularized LOWER, and the two monotonic branches of the limiting
comparator rate. No finite monotonicity of individual coefficients is assumed.

The [portable exact-field audit](../experiments/audit_research_cap_cross_all_demand_subexponential_contraction.py)
with [recorded results](../experiments/research_cap_cross_all_demand_subexponential_contraction_results.json)
checks N=3 through 10: 164 literal coefficient-contiguity identities and
52 original projected flux recurrences, including both parity cutoffs and
empty terminal ranges. It separately checks 52 full raw physical
three-port scalars, 52 full auxiliary recurrences, 24 actual low-cutoff
identifications and 52 Newton resolvent entries. All calculations are
exact in the chosen finite fields, with conservative integer-overflow
bounds. These are finite source-identity checks, not an asymptotic proof.
The subexponential estimates are established analytically above.
Root completed a fresh redirected replay of this combined finite
audit with identical recorded results.
