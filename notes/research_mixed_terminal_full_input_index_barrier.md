# The ordinary-index barrier on both full typed input disks

Research deduction, 6 November 2026. The ordinary main index preceding
a selected terminal input can be restricted to \(s_R\ge.22\) on
both entire original typed input disks. The proof uses a degree-six
polynomial with an elementary endpoint-minimum argument, retaining the
incoming chirp. A separate curvature corollary preserves the three
scalar gains by dropping an unused incoming curvature reserve; it does
not extend the older half-outer-curvature lemma beyond its domain.
No reference, primitive, optimizer or parameter cover is evaluated.

## 1. Exact derivative and scalar reduction

Use the original own-four phase
\[
 Q_1(s;b,a)=g(s+b)+g(s+a)-3g(s)-g(b)-g(a)+2\pi ibs.
 \tag{1}
\]
Write \(b=x+ih_b\), \(a=y+iH\), \(s=\sigma+ih_s\), and assume
\[
 x,y\in P=[.22,.45],\quad -.12\le h_b\le.08,\quad
 -.102\le h_s\le-.001,\quad 0\le H\le.014.
 \tag{2}
\]
The lower bound on \(h_b\) in (2) is only needed to invoke the
existing full-domain concavity after proving the derivative at .22.
It is not used in that derivative estimate.

**Theorem 1.** On (2),
\[
 \Re Q_{1,s}(.22+ih_s;b,a)>\frac1{40}.
 \tag{3}
\]
Consequently \(\Re Q_{1,s}>1/40\) for
\(.125\le\sigma\le.22\). Any joint main profile whose other
terms are independent of \(s\) has its maximum on
\(.22\le\sigma\le.5\).

*Proof.* Put \(R=e^{2\pi h_s}\), \(T=e^{-2\pi h_b}\), and
\(W=e^{2\pi H}\). The original chirp gives exactly
\[
 e^{2\Re Q_{1,s}}=
 \frac{\left[T^2+R^2-2TR\cos(2\pi(\sigma+x))\right]
       \left[1+R^2W^2-2RW\cos(2\pi(\sigma+y))\right]}
      {\left[1+R^2-2R\cos(2\pi\sigma)\right]^3}.
 \tag{4}
\]
In particular the factor \(T\) results from the retained
\(-2\pi h_b\) in \(\Re Q_{1,s}\); dropping that chirp would
give a different expression.

At \(\sigma=11/50\), the following strict bounds suffice:
\[
 \frac12<R<1,\qquad T>\frac35,\qquad W\ge1,
 \quad \cos(2\pi\sigma)>\frac9{50},\quad
 \cos(2\pi(\sigma+x)),\cos(2\pi(\sigma+y))<-\frac9{20}.
 \tag{5}
\]
For explicit elementary witnesses, the original
[shape half-plane lemma](research_mixed_reference_shape_half_plane.md)
proves \(e^{17/25}<2\), while \(.204\pi<17/25\), giving
the bound for \(R\). Also \(.16\pi<101/200\), and the
positive exponential series gives
\[
 e^{101/200}
 \le1+\frac{101}{200}
       +\frac{(101/200)^2}{2(1-101/600)}
 =\frac{331001}{199600}<\frac53,
 \qquad \frac53-\frac{331001}{199600}
                       =\frac{4997}{598800}>0.
 \tag{6}
\]
Here the tail bound uses \(n!\ge2\cdot3^{n-2}\) for
\(n\ge2\). This proves the bound for \(T\), including the
largest allowed positive incoming height.

Next \(\cos(.44\pi)=\sin(.06\pi)>
3/16-(3/16)^3/6=1527/8192>9/50\).
For \(z\in P\), the maximum of
\(\cos(2\pi(.22+z))\) is \(-\sin(.16\pi)\).
Since \(.16\pi>1/2\),
\(\sin(.16\pi)>1/2-(1/2)^3/6=23/48>9/20\).
These comparisons use only \(157/50<\pi<22/7\) and the
alternating sine lower bound on the displayed intervals.

The two numerator factors in (4) therefore exceed
\(R^2+27R/50+9/25\) and
\(R^2+9R/10+1\), respectively. The denominator base is less
than \(D(R)=R^2-9R/25+1\). Let
\[
\begin{split}
 P_6(R)&=(R^2+27R/50+9/25)(R^2+9R/10+1)-D(R)^3\\
 &=-R^6+\frac{27}{25}R^5-\frac{1493}{625}R^4
       +\frac{56979}{15625}R^3-\frac{3857}{2500}R^2
       +\frac{243}{125}R-\frac{16}{25}.
\end{split}
 \tag{7}
\]
This polynomial is bounded below by its smaller endpoint value
on \([1/2,1]\). Indeed
\[
 P_6'''(R)=-120R^3+\frac{324}{5}R^2
                       -\frac{35832}{625}R+\frac{341874}{15625}
 \le-\frac{31026}{15625}<0,
 \qquad P_6'(1/2)=\frac{130737}{62500}>0.
 \tag{8}
\]
For the inequality in (8), combine the first two terms as
\(R^2(324/5-120R)\le24/5\), and use \(R\ge1/2\)
in the negative linear term. Thus \(P_6'\) is strictly concave
and positive at the left endpoint. Its nonnegative set is an interval
containing that endpoint, so \(P_6\) first increases and may then
decrease; it has no interior minimum. The exact endpoint values are
\[
 P_6(1/2)=\frac{270957}{1000000},\qquad
 P_6(1)=\frac{68691}{62500}.
 \tag{9}
\]

Since \(D(R)\le41/25\), equations (4)--(9) imply
\[
 \Re Q_{1,s}>
 \frac12\log\left(1+\frac{270957}{4410944}\right)
 >\frac{270957}{9363802}>\frac1{40}.
 \tag{10}
\]
The middle inequality is \(\log(1+u)>u/(1+u)\) for
\(u>0\); the last has positive cross-product difference
\(1474478\). Finally the bare ordinary Hessian bound in
[the plateau compiler](research_mixed_plateau_window_concave_profiles.md),
equation (9), gives \(\Re Q_{1,ss}<0\) throughout
\([.125,.5]+ih_s\) with both outer arguments in
\(P+i[-.12,.12]\). Moving left from .22 increases this
derivative, proving the remaining claims. \(\square\)

Both full typed disks
\(D_3=\{|b-(.35-.01i)|\le.09\}\) and
\(D_4=\{|b-(.30-.052i)|\le.064\}\) lie inside the incoming
rectangle in (2). Thus no additional coupled-reference filter is
needed for this barrier. The actual terminal private coordinate,
the terminal factor, both complete selected-weight alternatives and
the incoming affine marginal are unchanged by the move in \(s\).

## 2. Preserve the three needed costs without an enlarged old lemma

The older retained-half-outer pair lemma assumes both height moduli
are at most .102. That lemma is not asserted for an input at the
bottom of \(D_4\), where \(h_b=-.116\). Instead use only
positivity for the pair incident to that external input.

**Lemma 2.** For \(V(s,b)=g(s+b)-g(s)-g(b)\),
\[
 -\Re V(s,b)''\succeq0
 \quad\text{if}\quad
 \Re s\in[.22,.5],\ \Re b\in P,\
 |\Im s|,|\Im b|\le.12.
 \tag{11}
\]
In fact the form is positive definite on this closed product.

To see this, both real cotangents are nonnegative and that of \(b\)
is positive. Also
\(\cos(2\pi\Re s),\cos(2\pi\Re b)<1/5\), whereas
\(e^{-2\pi|\Im s|},e^{-2\pi|\Im b|}>1/3\), since
\(.24\pi<1\) and \(e<3\). The identity
\[
 |\Im\cot\pi z|<1
       \quad\Longleftrightarrow\quad
 \cos(2\pi\Re z)<e^{-2\pi|\Im z|}
 \tag{12}
\]
therefore applies to both coordinates. Proposition 1 of
[the exact pair-curvature identity](research_mixed_pair_curvature_composition.md)
proves (11), including \(\Re s=.5\).

Now use the original joint terminal main phase, retain all terminal
height hypotheses from the
[three-cost theorem](research_mixed_terminal_joint_main_curvature_budget.md),
and replace only its incoming-height restriction by (2). The new
barrier supplies \(s_R\ge.22\), and the existing terminal barrier
supplies \(t_R\ge.18\). Decompose the ordinary term exactly as
\[
 Q_1=V(s,b)+V(s,a)-g(s)+2\pi ibs.
 \tag{13}
\]
Use Lemma 2 for \(V(s,b)\). Use the old retained-half-outer
lemma only for \(V(s,a)\), where the actual height moduli still
satisfy \(|h_s|\le.102\), \(|H|\le.014\). Combine these
with the terminal private-pair estimate and unchanged weights.
In the order \((b,s,a,t,v)\) the resulting valid matrix bound is
\[
 -\Re D_\nu''\succeq\operatorname{diag}\left(
 \frac\beta2g_{h_b}''(b_R),\
 g_{h_s}''(s_R),\
 (\nu+\tfrac12)g_H''(a_R),\
 g_{h_t}''(t_R),\ 0\right).
 \tag{14}
\]
The first entry is deliberately smaller than the old
\((1+\beta)g_{h_b}''/2\). No extension of that old incoming
reserve is used.

**Corollary 3.** At \(H=.01\), the same three-gain budget (12)
of the curvature theorem is valid for every incoming height in (2),
with all its other original hypotheses unchanged. Its scalar
sufficient criterion (13)--(19) therefore needs no narrower
incoming-height guard.

Indeed the original lifted-reference gradient is still
\((0,A_s,A_{a,\nu},A_t,0)\). The incoming force is zero, so the
incoming convex cost was never needed in the three scalar maximizations.
All three retained costs in (14) are exactly the old ones. The same
argument also extends the full-\(P\) forced budget in
[the common-height criterion](research_mixed_terminal_joint_main_common_height.md)
when its additional scalar guards hold.

This proves an extended analytic criterion, not that its scalar
guards hold on the whole input disks. It does not change the separate
ordinary last-row/left-row/half-row domination domains, establish any
other terminal-profile sign, or supply a full finite-source estimate.
The boundary correction in
[one-parameter transport](research_mixed_terminal_one_parameter_transport.md)
remains required for a boundary-only uniform argument.
