# The complete long lower right side of the original cap contour

Research deduction, 8 November 2026. A positive bound on every
original auxiliary row pays the lower weighted side from private
height \(-3/50\) to \(-1\). At the incoming wall its lower auxiliary
half has rate less than \(4129/6000\); its upper auxiliary half has
nonpositive rate. A uniform real-index derivative bound transports
the same complete estimate to the existing right cut.

No endpoint packet is assumed at these larger negative heights.
All revived rows and original carriers remain. This proves one
complete current, not an outer-cap or filled-source asymptotic.
No numerical evaluation or frozen-source edit is used.

## 1. Exact finite source and its weighted row rate

Use the original notation and exact carrier cancellation in
[the tall lower alias](research_mixed_cap_tall_lower_alias.md):
\[
 \mathscr A_N(e,a,w)=
 \sum_{l=0}^{N-1}\frac{e_l(w)}{S_l}\,
 e^{i\pi Ne(l/N-a)}
 \frac{G_N(N(a+e))}
      {G_N(Na)G_N(N(e-l/N))}.
 \tag{1}
\]
At the physical private index \(e=j/N\), this is exactly
\(H_N(w,r^{-j})p_j(e^{-2\pi ia})/P_j\). In particular (1)
contains every auxiliary term that revives off the physical grid.
Its normalization is the original \(D_N^{-1}C_N\) cap row.

Set
\[
 a=1-v,\quad 3/10\le v\le1/2,\quad
 e=E-iH,\quad 3/50\le H\le1,\quad u=l/N.
 \tag{2}
\]
Use the canonical lower primitive \(J_-\) from
[uniform half-plane factorial continuation](research_factorial_uniform_halfplane_continuation.md).
For \(w=-2\cos\theta\), the full zero-safe Newton estimate of
[the color-tube theorem](research_mixed_newton_color_tubes.md)
gives the weighted row upper rate
\[
\begin{split}
 \mathcal R(E,a,H,u)
  ={}&V_\theta(u)-J(u)-J(a)
       +\Re J_-(a+E-iH)-\Re J_-(E-u-iH)\\
    &+\pi H(u-a)-2\pi H.
\end{split}
 \tag{3}
\]
The penultimate term is the exact carrier in (1); the last is
the lower cotangent-remainder penalty. The full uniform factorial
theorem applies to both nonreal arguments on these fixed compact
sets, including negative real parts and points above the reflected
reciprocal wall. The real argument \(a\) stays in its original
compact strip. The uniform physical \(S_l\) estimate holds through
both true auxiliary ends.

Thus each literal row, including its weighted kernel, is bounded
by a polynomial in \(N\) times \(e^{N\mathcal R}\), uniformly
over all original \(l\), ordinary real colors and both parities.
At a Newton zero this is an upper bound without division.
The \(N\)-term sum and the original residue density \(+N\) have
only polynomial cost.

The inherited envelopes and constants used below are
\[
\begin{gathered}
 V_\theta(u)\le V_0(u)\le b_2<73/125
                    \quad(0\le u\le1/2),\\
 V_\theta(u)\le0\quad(1/2\le u\le1),\qquad
 -J(u)\le1/6,\\
 b_2=-4J(1/4)<7/12.
\end{gathered}
 \tag{4}
\]
The last sharper inequality, with its finite logarithmic/Catalan
witness, is written in equations (14)--(15) of
[the low-index kernel margin](research_mixed_next_low_index_kernel_margin.md).
It is used only for the quotient maximum below. All these are
already established scalar inequalities, not new source evaluations.

## 2. The whole lower auxiliary half at the wall

First put \(E=v\). The actual lower primitive satisfies
\[
 \Re J_-(1-iH)=\pi H/2,\qquad J(a)=-J(v).
 \tag{5}
\]
These follow from its fixed formula and real reflection.
For \(0\le d\le1/2\),
\[
 J(d)-\pi H/2\le\Re J_-(d-iH)=\Re J_+(d+iH)\le J(d).
 \tag{6}
\]
Indeed its height derivative is
\(-\Arg\sin\pi(d+iH)\in[-\pi/2,0]\).
The continuous endpoint \(d=0\) has
\(\Re J_+(iH)=-\pi H/2\), so is included.
The exact reflected identity for \(d\ge0\) is
\[
 -\Re J_-(-d-iH)=\Re J_+(d+iH)+\pi H.
 \tag{7}
\]
The term \(\pi H\) in (7) is compulsory; no periodic factor is
discarded.

For \(0\le u\le v\), equations (3), (5), and the lower bound
in (6) give
\[
 \mathcal R(v,a,H,u)
 \le V_\theta(u)+J(v)-J(u)-J(v-u)
                     -\pi H(2-u-v).
 \tag{8}
\]
The exact quotient maximum is
\[
 J(v)-J(u)-J(v-u)\le A(v):=J(v)-2J(v/2)
       \le A(1/2)=-2J(1/4)<7/24.
 \tag{9}
\]
The midpoint is the maximum by symmetry and strict concavity
of the quotient on \(0<u<v\). Also
\(A'(v)=\log(2\cos(\pi v/2))>0\) on this range.
Since \(u+v\le1\), \(H\ge3/50\), and \(\pi>25/8\), (4)
and (8)--(9) imply
\[
 \mathcal R(v,a,H,u)
 <\frac{73}{125}+\frac7{24}-\frac3{16}
                      =\frac{4129}{6000}.
 \tag{10}
\]

For \(v\le u\le1/2\), put \(d=u-v\in[0,1/5]\).
Use (7) and the upper bound in (6), retaining every height
term in (3):
\[
 \mathcal R(v,a,H,u)
 \le V_\theta(u)-J(u)+J(d)+J(v)
                        -\pi H(3/2-u-v).
 \tag{11}
\]
Here \(J(d),J(v)\le0\) and \(u+v\le1\). Thus
\[
 \mathcal R(v,a,H,u)
 <\frac{73}{125}+\frac16-\frac3{32}
   =\frac{7883}{12000}<\frac{4129}{6000}.
 \tag{12}
\]
Both formulas agree at the reflected wall in the required
upper-bound sense. They apply to every literal auxiliary row,
not only to the old physically terminating triangle.

## 3. Every revived upper-half auxiliary row

For \(1/2\le u\le1\), (4)--(5) and (7) give
\[
 \mathcal R(v,a,H,u)\le K(u):=
 -J(u)+J(v)+\Re J_+(u-v+iH)
                           +\pi H(u+v-3/2).
 \tag{13}
\]
This upper profile is strictly convex on \(1/2<u<1\):
\[
 K''(u)=\pi\{\Re\cot\pi(u-v+iH)-\cot\pi u\}>0.
 \tag{14}
\]
If \(u-v\le1/2\), the first real cotangent is nonnegative,
whereas the second is nonpositive. If \(u-v>1/2\), its
negative real cotangent is increased by the nonzero height,
so
\(\Re\cot\pi(u-v+iH)>\cot\pi(u-v)>\cot\pi u\).
This proves (14) on both portions.

At \(u=1/2\), (6) gives
\[
 K(1/2)=J(v)+\Re J_+(1/2-v+iH)+\pi H(v-1)\le0.
 \tag{15}
\]
At the other endpoint, the original reflection gives
\[
 K(1)=J(v)-\Re J_+(v+iH)+\pi H(v-1/2)\le0.
 \tag{16}
\]
To verify the last sign, its value at \(H=0\) is zero and
its height derivative is
\[
 \Arg\sin\pi(v+iH)+\pi(v-1/2)\le0,
 \tag{17}
\]
because
\(\Arg\sin\pi(v+iH)=
\arctan(\cot(\pi v)\tanh(\pi H))\le\pi(1/2-v)\).
For \(v=1/2\), the endpoint identity remains exact.
Convexity and continuity at the logarithmic end \(u=1\)
therefore give \(K(u)\le0\) throughout the whole upper half.
No complete-color-only entropy has replaced the all-real
inequality \(V_\theta\le0\).

Combining (10), (12), and (13)--(17), the entire original
positive auxiliary sum at the wall has weighted rate less than
\(4129/6000\), uniformly in \(a,H\) and every real color.

## 4. Transport to the unchanged upper proof cut

For any real \(E\), differentiating the actual rate (3) gives
\[
 \partial_E\mathcal R
   =\log\left|
       \frac{\sin\pi(a+E-iH)}{\sin\pi(E-u-iH)}
          \right|.
 \tag{18}
\]
No carrier term depends on \(E\) in this modulus derivative.
For every real \(x\),
\[
 \sinh(\pi H)\le|\sin\pi(x-iH)|\le\cosh(\pi H).
\]
It follows that
\[
 |\partial_E\mathcal R|
       \le\log\coth(\pi H)<2\qquad(H\ge3/50).
 \tag{19}
\]
Here \(\pi H>3/16\), and
\[
 e^{3/8}>1+\frac38+\frac9{128}=\frac{185}{128}>\frac75
\]
implies \(\coth(3/16)<6\). Finally \(e^2>1+2+2+4/3>6\)
gives \(\log6<2\). This is a direct elementary witness,
independent of any source or action evaluation.

Keep precisely the cut of
[the complete upper-end theorem](research_mixed_cap_upper_end_currents.md):
\[
 b(a)=\min\{49/100,v-\delta\},\qquad 0<\delta<1/100.
 \tag{20}
\]
Its former fixed collar and critical-point conditions remain
unchanged. For every \(v\in[3/10,1/2]\),
\[
                       0\le v-b(a)\le1/100.
 \tag{21}
\]
Thus (18)--(21) transport each literal row, including its
full reciprocal factor, from the wall to the chosen cut with
rate cost at most \(1/50\). We obtain
\[
 \mathcal R(b(a),a,H,u)
       <\frac{4129}{6000}+\frac1{50}
        =\frac{4249}{6000},
 \qquad 0\le u\le1,\quad3/50\le H\le1.
 \tag{22}
\]
This simultaneously handles the old \(49/100\) cut and the
moving wall cut. The half-plane primitives in (18) remain
regular even when \(E-u\) passes through zero.

The already proved original action floor in
[the long upper right-side theorem, equation (8)](research_mixed_cap_upper_right_long_side.md)
is \(M(a)=\Re\mathcal T(a)>43/60\). It follows that
\[
               M(a)-\frac{4249}{6000}>\frac{17}{2000}.
 \tag{23}
\]
This is a uniform actual-action comparison, not a comparison
with a separately normalized terminal source.

## 5. The complete weighted side and derivatives

At each base \(a\), use the original half-grid boundary
\[
 b_N=(\lceil Nb(a)\rceil-1/2)/N.
 \tag{24}
\]
Its \(O(N^{-1})\) displacement costs only \(O(1)\) in the
exponent by (19). On the lower side the exact cotangent
remainder has modulus at most \(2e^{-2\pi NH}\).
This is precisely the penalty already included in (3);
the original orientation and density \(+N\) are retained.

**Theorem.** The entire original weighted right-side current
between \(b_N-3i/50\) and \(b_N-i\) satisfies
\[
       |\mathcal V^-_{N,\mathrm{right,long}}(a,w)|
       \le C N^B e^{N\{M(a)-1/250\}}
 \tag{25}
\]
uniformly for \(a\in[1/2,7/10]\), every real ordinary color
\(w\in[-2,2]\), and both level parities. Every original
auxiliary term and every Newton/reciprocal zero is included.

Indeed the uniform factorial errors, \(N\) auxiliary rows,
bounded side length and density are polynomial costs.
One common tolerance and absorption of these factors fit
strictly inside the reserve (23). This proves (25) from
literal positive row bounds; no estimate on a signed complete
coefficient has been assigned to its individual terms.

The Newton color-tube theorem gives every fixed ordinary
derivative with polynomial cost and preserves (22) on small
fixed complex ordinary-color disks with an arbitrarily small
extra rate. All nonreal factorial arguments stay in their
proved half-plane compact domains under small complex
incoming perturbations. Fix each base cut and side first,
use the original holomorphic cap critical action there, and
apply Cauchy's formula on smaller neighborhoods. This gives
every fixed normalized mixed jet, for example with gap
\(1/500\). No derivative of the moving cutoff is taken.

The old short lower right side from the real cut to depth
\(3/50\) is paid by its own complete endpoint theorem.
Together with (25), this pays the full lower right sign-half
of a residue rectangle reaching depth one. The lower horizontal
alias has its separate complete estimate. No new unweighted
connector, left current, or main-path contribution is deleted.
These remain the exact currents of the original cap identity.
