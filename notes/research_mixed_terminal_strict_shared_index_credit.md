# A strict saving from opposed forces at a shared index

Research deduction, 6 November 2026. The shared-index comparison can
give a strictly negative contribution, rather than merely no additional
cost. The proof uses a lower bound on the increase of the exact scalar
conjugate. It does not subtract a numerical upper bound as if it were
a lower bound. No new source or analytic evaluation is used here.

## 1. The exact cost

Use the original function \(g_h(x)=\Re g(x+ih)\) and put
\[
 I=[11/50,1/2],\qquad 6/25\le A\le x_*\le B\le9/25,
 \qquad |h|\le27/250,\qquad k>0.
\]
Define
\[
 \phi(x)=k\{g_h(x)-g_h(x_*)-g_h'(x_*)(x-x_*)\},\qquad
 G(q)=\max_{x\in I}\{q(x-x_*)-\phi(x)\}.
 \tag{1}
\]
The [shared-index reflection lemma](research_mixed_terminal_shared_index_gain_cancellation.md)
proves \(G(-q)\le G(q)\) for \(q\ge0\).
Every statement below concerns the same exact center, height, coefficient
and target interval in (1).

Set
\[
 M=k/A,\qquad D=1/2-B>0,
 \qquad
 L(q)=
 \begin{cases}
 q^2/(2M),&0\le q\le MD,\\
 Dq-MD^2/2,&q\ge MD.
 \end{cases}
 \tag{2}
\]
The function \(L\) is continuously differentiable, with
\(L'(q)=\min(q/M,D)\).

**Lemma 1.** If \(0\le q_1\le q_2\), then
\[
                 G(q_2)-G(q_1)\ge L(q_2)-L(q_1).
 \tag{3}
\]

*Proof.* For \(x\in[x_*,1/2]\), the exact curvature formula gives
\[
 0\le g_h''(x)
 =\frac{\pi\sin(2\pi x)}{\cosh(2\pi h)-\cos(2\pi x)}
 \le\pi\cot(\pi x)\le\frac1x\le\frac1A.
 \tag{4}
\]
The penultimate inequality follows from \(\tan t\ge t\) on
\([0,\pi/2)\); the endpoint \(x=1/2\) follows by continuity.
Consequently \(\phi''\le M\) on this interval.

For a nonnegative force, a maximizing target may be taken to the right
of the center: every target to the left has nonpositive objective,
whereas the center has objective zero. Write the right displacement as
\(d\in[0,D_*]\), where \(D_*=1/2-x_*\ge D\), and set
\(p(d)=\phi(x_*+d)\). Then \(p'(0)=0\), and integration of
(4) gives \(p'(d)\le Md\). The curvature is strictly positive
before the right endpoint. Thus the maximizing displacement is unique:
it solves \(p'(d)=q\) if this equation has a solution in the interval,
and is \(D_*\) if \(q\ge p'(D_*)\). In either case
\[
                         d(q)\ge\min(q/M,D).
 \tag{5}
\]
The inverse of the strictly increasing function \(p'\), followed by
the constant endpoint value, is continuous. Differentiating the
maximized expression gives \(G'(q)=d(q)\), also at the transition
to the endpoint. Integrating (5) proves (3). \(\square\)

## 2. A negative shared-index contribution

Let \(u=-a<0<v\). The quantity needed when composing the two height
changes is the signed difference \(G(v-a)-G(v)\).

**Proposition 2.** If \(0<a<2v\), then
\[
 G(v-a)-G(v)
 \le-\{L(v)-L(|v-a|)\}<0.
 \tag{6}
\]

*Proof.* Reflection gives \(G(v-a)\le G(|v-a|)\), with equality
in this step when \(v-a\ge0\). The hypothesis gives
\(0\le|v-a|<v\), so Lemma 1 applies. Since \(D,M>0\),
the function \(L\) is strictly increasing for positive arguments.
This proves both inequalities in (6). \(\square\)

There is a version using only enclosing force intervals. Suppose
\[
 0<a_-\le a\le a_+<2v_-,\qquad v\ge v_->0,
 \qquad \delta=\min\{a_-,2v_--a_+,v_-\}>0.
 \tag{7}
\]
Then
\[
 G(v-a)-G(v)
       \le-\{L(v_-)-L(v_--\delta)\}<0.
 \tag{8}
\]
Indeed \(v-|v-a|=\min\{a,2v-a\}\ge\delta\). The derivative
\(L'\) is nonnegative and nondecreasing, so an interval of length
at least \(\delta\) ending at \(v\ge v_-\) has integral at least
\(L(v_-)-L(v_--\delta)\). Combine this with (6).

## 3. What this would contribute to the source estimate

For the exact shared cost in the two-selected terminal window,
\(k=2\). The existing general reference bounds permit
\(A=6/25\), \(B=9/25\), hence \(M=25/3\) and \(D=7/50\).
Sharper proved center bounds may replace these constants.
No scalar gain or transcendental function needs to be evaluated
to use (8) once its force bounds have been proved.

The [composition theorem](research_mixed_terminal_two_selected_budget_composition.md)
contains the exact term \(G(u+v)-G(v)\). Under (7), its upper
bound can therefore retain the negative number in (8). This is
stronger than replacing that term by its positive part.

Neither (7) nor a negative total ordinary-lift budget is established
for the entire canonical reference family here. The separate fixed
two-budget calculation retains its already specified nonnegative
linear debit and does not use this deduction. This scalar saving
also does not prove a lower bound for the original quantum sum;
that still requires its geometric contribution and all competing
terms to be controlled.
