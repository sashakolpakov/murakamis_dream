# A common higher contour for both terminal main alternatives

Research deduction, 6 November 2026. The forced main phase retains
the same ordinary-index and terminal-index convex costs as the factorial
phase. This supplies a full-selected-interval upper bound, which can
be transported to a higher height together with the factorial bound.
The resulting criterion compares both alternatives on the same contour.
No new reference, primitive or target optimization is used.

## 1. A full-interval forced budget at the original height

Use the original \(D_\nu,T_\nu,A_s,A_t,A_{a,\nu}\), action,
incoming complex marginal, and allocation from
[the joint-main theorem](research_mixed_terminal_joint_main_budget.md).
Set \(H_0=1/100\), \(P=[.22,.45]\), \(a_*=A+ic\),
and \(d=.5-\Re s_*\). Retain all hypotheses (1) and (13) of
[the curvature-budget theorem](research_mixed_terminal_joint_main_curvature_budget.md).
In particular the original reference is stationary, the legitimate
main-maximizing intervals are \(s_R\in[.22,.5]\), \(t_R\in[.18,.5]\),
and its three force/coordinate guards apply.

The simultaneous matrix allocation in that theorem, equation (11),
holds for the forced phase on **all** \(a_R\in P\): its selected
scalar convex cost has coefficient \(1/2\), which is nonnegative.
Discard only that cost, retain the other two, and keep both boundary
and private coordinates free. If \(A_{a,0}\ge0\), it follows that
\[
 \sup_{\text{full original main product}}D_0(H_0)
 \le B_0:=
 T_0+\frac{15A_s^2}{128d}+\frac{A_t^2}{3}
                         +A_{a,0}(.45-A).
 \tag{1}
\]
This is not limited to the earlier forced interval \([.4,.45]\).
Indeed the full-\(P\) affine support of its nonnegative selected force
uses the same right endpoint \(.45\). The scalar \(s\)- and \(t\)-gain
bounds follow from equations (14)--(17) of the curvature theorem.
The omitted selected convex remainder is nonnegative because its
center \(A\) belongs to \(P\). This omission does not alter any
other Hessian contribution.

More generally replace the last term in (1) by
\(\max\{A_{a,0}(.22-A),A_{a,0}(.45-A)\}\) if the selected
force has either sign. No sign assumption is then necessary.
Let \(B_1\) be any proved factorial upper bound at the same height
\(H_0\), on the entire original main product.

## 2. Same-height transport of the complete rate maximum

Keep all original heights except \(a_R+iH\), with
\(H_0\le H\le7/500\). Write
\(\mathcal A(y,k)=\Im g'(y+ik)=\arg(1-e^{2\pi k-2\pi iy})\).
The two original derivatives are
\[
 \begin{split}
 \partial_HD_1={}&-\mathcal A(s_R+a_R,h_s+H)
             -\mathcal A(t_R+a_R,h_t+H)
             +3\mathcal A(a_R,H)-2\pi t_R-2\pi,\\
 \partial_HD_0={}&-\mathcal A(s_R+a_R,h_s+H)
             -\mathcal A(t_R+a_R,h_t+H)
             +2\mathcal A(a_R,H)-2\pi t_R .
 \end{split}
 \tag{2}
\]
The shared chirp and complete selected monomial are unchanged.
The original index barrier restricts every maximum, for both
alternatives and every height in this interval, to \(t_R\ge.18\).
This is the same common target restriction used in
[the height-monotonicity theorem](research_mixed_terminal_joint_main_height_monotonicity.md).

That theorem gives \(\partial_HD_1<-11/10\) on the common restricted
product. Its same argument bounds also give
\[
 \partial_HD_0<
 \begin{cases}
 (98/75)\pi+3/100<1241/300,&a_R\le.4,\\
 (16/25)\pi+19/10<1369/350<1241/300,&a_R\ge.4 .
 \end{cases}
 \tag{3}
\]
For the first line, the two summed arguments exceed
\(-\pi/2\) and \(-\pi/2-.03\), respectively, while the own
argument is less than \(\pi/3\). For the second they exceed
\(-\pi/2-1/3\) and \(-\pi/2-5/6\), and the own argument is
less than \(11/30\). These estimates hold on the full real
\(s\)-interval and all \(a_R\in P\), with the original height
upper bounds \(h_s\le-.001,\ h_t\le.021\).

Set \(\delta=H-H_0\). The complete selected-weight main rate has
the rigorous common-height upper bound
\[
 \sup_{a_R\in P,\ \text{other main targets}}
                   \max\{D_1(H),D_0(H)\}
 \le
 \max\left\{B_1-\frac{11}{10}\delta,\
                 B_0+\frac{1241}{300}\delta\right\}.
 \tag{4}
\]
This follows by integrating (2)--(3) at fixed real targets, then
maximizing on the common restricted product. Both bounds in (4)
belong to \(H\). The exact selected polynomial retains its additive
factorial-plus-forced estimate; the rates are never replaced by
their minimum, nor is either physical summand deleted.

For a desired gap \(\gamma>0\), a concrete sufficient condition is
that the interval
\[
 [0,1/250]\ \cap\
 \left[\frac{10}{11}(B_1+\gamma),\
                         \frac{300}{1241}(-B_0-\gamma)\right]
 \tag{5}
\]
contain a point, with strict inequalities where a strict gap is needed.
This is a criterion on the original correlated reference and its
already proved budgets. It requires no claim that the forced phase
decreases with height.

## 3. Explicit rational sufficient guards

In addition to the curvature theorem's hypotheses, suppose the saved
or otherwise certified values at \(H_0\) satisfy
\[
 T_0<-\frac{109}{1000},\qquad
 0<A_{a,0}<\frac{63}{200},\qquad
 A>\frac7{25}.
 \tag{6}
\]
The same existing scalar bounds then give
\[
 B_0<
 -\frac{109}{1000}+\frac{19881}{1587200}
       +\frac{867}{40000}+\frac{1071}{20000}
 =-\frac{843167}{39680000},
 \qquad B_1<-\frac{50063}{39680000}.
 \tag{7}
\]
Choose the single common height \(H=27/2000=.0135\), so
\(\delta=7/2000\). Equations (4) and (7) give
\[
 \begin{split}
 \sup D_1(H)&<-\frac{202831}{39680000}
                 <-\frac1{200},\\
 \sup D_0(H)&<-\frac{4030001}{595200000}
                 <-\frac1{200}.
 \end{split}
 \tag{8}
\]
The respective exact reserves beyond \(1/200\) are
\(4431/39680000\) and \(1054001/595200000\).
Thus (6), together with the earlier explicit curvature guards,
is a sufficient uniform criterion for both main alternatives
at a common higher contour.

The four previously certified canonical references are candidates for
this application: their earlier curvature guards are already audited,
and (6) uses only entries of the unchanged saved diagnostic.
A separate exact saved-data guard check is required to record that
application. Equations (1)--(8) themselves are analytic implications,
not a new evaluation or a full-reference-domain cover.

## 4. A reusable continuous forced-domain cutoff

Although (4) bounds the forced phase on all of \(P\), one can sharpen
other profile comparisons without assigning it the same large interval
at every height. Put \(w_H(x)=-\Re g(x+iH)-2\pi H\).
For \(0\le H\le7/500\), define
\[
 x_0(H)=
 \frac{8/25-(33/7)H}{16/25+(22/7)H}.
 \tag{9}
\]
Then \(w_H(x)>0\) for every \(x\in P\) with \(x\le x_0(H)\).
Consequently the forced alternative need only be considered on
\(P\cap[x_0(H),.45]\), possibly an empty interval.
The factorial alternative keeps all of \(P\).

To prove this, let \(L(x)=\log(2\sin\pi x)\).
It is concave on \((0,1)\). Hence
\(-J(x)=\int_x^{1/2}L(t)\,dt\ge
(\frac12-x)\{L(x)+\log2\}/2\).
The [existing cutoff proof](research_mixed_selected_weight_branch_domains.md)
gives \(L(9/25)>59/100\), and
\(\log2=2\operatorname{atanh}(1/3)>56/81>69/100\).
For \(9/25\le x\le.45\) this yields
\[
 w_H(x)>
 \frac{16}{25}\left(\frac12-x\right)
                      -\frac{22}{7}H\left(\frac32+x\right).
 \tag{10}
\]
The vertical contribution is exactly the favorable one retained in
equation (4) of the existing cutoff proof. The right side of (10)
vanishes at (9). Moreover \(x_0(H)\ge x_0(.014)=127/342>9/25\).
The already proved monotonicity of \(w_H\) in \(x\) extends the
positivity to all smaller \(x\in P\). If \(x_0(H)>.45\), apply
(10) at \(.45\) instead. This also handles \(H=0\).
At \(H=.01\), \(x_0=191/470\), and at \(H=.014\),
\(x_0=127/342\).

The exact restricted-branch supremum identity from the existing
branch-domain theorem therefore holds with these height-dependent
cutoffs, including for any fixed finite product of selected weights.
This changes a domain of upper-rate comparison, not a source sum.
Neither this cutoff nor (4) controls the other 26 terminal profiles,
the outer cycles, or a nonzero complete-source coefficient.
