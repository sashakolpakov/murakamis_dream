# Coherent physical tails for the prepared three-four cap

Research deduction, 7 November 2026. The original complete-boundary
coefficient already has a whole-sum asymptotic on every compact real
index interval inside \((0,1)\). Using that coefficient before
taking absolute values improves the physical-tail problem for the
prepared three-four cap to eight concave faces and an explicit far
ceiling. The two true index endpoints are bounded separately from
their literal finite sums. No critical value, face bound, or new
analytic function has been evaluated here.

Use the exact source and notation of
[the prepared-cap source theorem](research_mixed_prepared_three_four_cap_source.md).
The output is fixed initially at \(y=x_0\), with
\(K=e^{2\pi ix_0}\), \(\rho=|K|\). The inherited
alternating parameter satisfies \(3/5<\rho<5/8\).
Put
\[
 L(q)=q\log\rho-\int_0^q\log|1-Ke^{-2\pi iv}|\,dv,
 \qquad \lambda(s)=\Re S(s,-2).
 \tag{1}
\]
All appearances of \(J\), \(S\), and the endpoint coefficient
use their original continuations and additive constants.

## 1. A coherent coefficient bound on the whole compact middle

Theorems 1--2 of
[the full real-index endpoint theorem](research_complete_boundary_full_index_interval.md)
prove, for every compact \(I\subset(0,1)\), the actual finite
coefficient asymptotic
\[
 b_{j,N}(-2)=\delta_j^{-1}N^{-3/2}
       A(j/N)e^{NS(j/N,-2)}(1+O_I(N^{-1})),\qquad j/N\in I.
 \tag{2}
\]
Here \(|\delta_j|=1\) and \(A\ne0\). This is the full
oscillatory coefficient, including both level parities; it is not
the absolute sum of its Newton terms. The cited theorem also supplies
fixed ordinary jets and a fixed joint ordinary-color neighborhood
on each such compact interval. Thus, for any \(\eta>0\),
shrinking that neighborhood gives a uniform upper rate
\(\lambda(s)+\eta\). No uniform extension to \(s=0,1\)
is inferred from (2).

On the compact middle the supported four-index rows consequently
have the upper rate
\[
 \begin{split}
 E_\lambda(s,t,p,q)={}&\lambda(s)
 +J(s+t)+J(t+p)+J(p+q)-2J(t)-3J(p)-J(q)\\
 &-\tfrac12\log\rho+L(q),
 \end{split}
 \tag{3}
\]
on
\(\Omega=\{s,t,p,q\ge0:s+t\le1,t+p\le1,p+q\le1\}\).
The original zero-safe factorial upper bounds apply on every support
face, with polynomial losses. Exact prohibited sum-\(N\) rows
are zero. In (3) the boundary sum has already been performed before
modulus, whereas the remaining three index sums have not.

The endpoint derivative results in
[the original cap real-tail theorem](research_mixed_outer_cap_real_tails.md),
Section 2, give
\[
 \begin{gathered}
 \lambda''(s)<0\quad(0<s<1/2),\\
 \lambda'(.27)>27/50,\qquad \lambda'(.49)<-3/5,\\
 \lambda'(s)-J'(s)\le-\log4,
       \qquad\lambda'(s)\le-\log2\quad(1/2\le s<1).
 \end{gathered}
 \tag{4}
\]
The concavity assertion is independent of an actual outer cap
reference: the original endpoint saddle has
\(0<\Re u_c(s)<s<1/2\), and the negative real Hessian
of its two-variable phase is the positive form displayed in that
theorem. Its complex Schur complement gives the first line of (4).
The two numerical inequalities in the second line are already proved
source inputs, not new evaluations. The last line is the exact
continued endpoint derivative identity above one half.

It follows that \(\lambda\) has a unique maximum
\(\Lambda\) on \((0,1)\), attained in \((.27,.49)\).
For a useful unevaluated ceiling, the literal coefficient entropy
\[
 \mathfrak B(s)=\max_{0\le u\le s}
       \{\mathcal V(u)-J(u)-J(s-u)\},\qquad
 \mathcal V(u)=2\int_0^u\log(2|\cos\pi v|)\,dv-2J(u),
 \tag{5}
\]
satisfies
\[
          \lambda(s)\le\mathfrak B(s)<\frac35+\frac13
                         =\frac{14}{15},\qquad
                         \Lambda<\frac{14}{15}.
 \tag{6}
\]
Indeed \(\max\mathcal V<3/5\) and \(|J|<1/6\) are
the established uniform real-factorial bounds. Comparing the
nonzero asymptotic (2) with the literal upper sum (5) proves the
first inequality at each interior point. Strict inequalities hold
at the interior maximizer, giving the last assertion.

## 2. True endpoint strips have independent finite-source bounds

Fix once and for all
\(\delta=1/1000\). The exact physical coefficient sum,
including all fixed ordinary derivatives, gives
\[
 \begin{array}{ll}
 \mathfrak B(s)\le2\delta\log2-4J(\delta),
                                      &0\le s\le\delta,\\
 \mathfrak B(s)<3/5+\delta\log2,
                                      &1-\delta\le s\le1.
 \end{array}
 \tag{7}
\]
For the first inequality, \(J\) is decreasing on \([0,\delta]\)
and \(\mathcal V(u)\le2u\log2-2J(u)\).
For the second write \(s=1-d\), \(0\le d\le\delta\),
and use
\[
 \mathcal V(u)-J(u)-J(s-u)
   =\mathcal V(u)+J(u+d)-J(u)
                         \le\mathcal V(u)+\delta\log2.
 \tag{8}
\]
These are bounds on the original coefficients near their true
endpoints, not extrapolations of (2). The zero-safe Newton bounds
preserve them with any prescribed rate tolerance for a sufficiently
small fixed ordinary-color neighborhood.

For the coupled low strip, let \(E_{34}(0,t,p,q)\) be the
completed paired kernel's original physical rate at its first
index zero, with both external parameters equal to \(K\).
The new physical rate with (5) satisfies the exact comparison
\[
 E_{\mathfrak B}(s,t,p,q)
 \le E_{34}(0,t,p,q)+\tfrac12\log\rho
                           +3\delta\log2-4J(\delta).
 \tag{9}
\]
This uses only
\(J(s+t)-J(t)\le s\log2\); support at \(s=0\)
is preserved. The entire old face \(s=0\) belongs to the
physical complement bounded in
[the completed paired source](research_mixed_contracted_pair_full_kernel.md),
comparison (P). Its rate is at most \(2261/1500\).
This is a reuse of that established inequality after the explicit
comparison (9), not a claim that the prepared cap has the old phase.

The elementary bounds
\[
 \log2<7/10,\quad \log250<6,\quad
 J(\delta)\ge\delta\log(4\delta)-\delta>-7/1000,
 \quad \tfrac12\log\rho<-1/5
 \tag{10}
\]
therefore give a uniform low-strip ceiling
\[
             E_{\mathfrak B}<
 \frac{2261}{1500}-\frac15+\frac{301}{10000}
 =\frac{40123}{30000}<\frac{67}{50}.
 \tag{11}
\]
Here \(\log250<6\) follows from \(e>8/3\), and
\(\log(8/5)>2/5\) follows from
\(\log(1+x)>2x/(2+x)\), \(x>0\).

For the high strip, support forces \(t\le\delta\).
The unchanged high-\(q\) derivative of the original four source
permits decreasing any \(q>21/50\) to \(21/50\),
without changing \(s\) or losing its high-strip label.
This derivative is independent of the incoming boundary coefficient.
Now use
\[
 \begin{gathered}
 J(s+t)\le-J(\delta),\quad
 J(p+t)-J(p)\le\delta\log2,\quad
 -2J(t)\le-2J(\delta),\\
 J(p+q)-2J(p)-J(q)<2/3,\qquad
 -\tfrac12\log\rho+L(q)
       <(1/2+21/50)\frac{13}{25}=\frac{299}{625}.
 \end{gathered}
 \tag{12}
\]
The last bound uses
\(L(q)\le q\log(\rho/(1-\rho))\),
\(\rho/(1-\rho)<5/3\), and
\(-\log\rho<\log(5/3)<13/25\).
Together with (7) and (10), this proves
\[
 E_{\mathfrak B}
 <\frac35+\frac23+\frac{299}{625}
                  +\frac{14}{10000}+\frac{21}{1000}
 =\frac{3314}{1875}<\frac{177}{100}.
 \tag{13}
\]
All estimates are continuous at true coordinate ends. Polynomial
prefactors and the number of physical rows require only an
arbitrarily small final rate tolerance.

## 3. The coherent far-\(p\) region

On \(p\ge5/6\), support gives \(t,q\le1/6\).
The same elementary real-primitive ordering as in the paired-tail
proof gives
\[
 J(p+t)+J(p+q)-3J(p)\le-J(p)\le0.
 \tag{14}
\]
The remaining three primitive terms are bounded by \(2/3\).
Only one external cardinal incidence remains, so
\[
 E_\lambda\le\Lambda+\frac23+
                         \left(\frac12+\frac16\right)\frac{13}{25}
       =\Lambda+\frac{76}{75}<\frac{146}{75}.
 \tag{15}
\]
The old \(2261/1500\) far-tail value has not been copied.
Equation (15) retains the new ordinary-cap rate \(\lambda\).
Keeping the sharper symbolic \(\Lambda+76/75\) is also valid.

## 4. All remaining compact tails clip to eight concave faces

Define the new central real box, aligned with the proved prepared
main rectangle, by
\[
 C_{\mathrm{cap}}=[.27,.49]\times[.22,.5]\times[.2,.42]^2.
 \tag{16}
\]
Consider a point of
\(\Omega\setminus\operatorname{int}C_{\mathrm{cap}}\)
with \(\delta\le s\le1-\delta\) and \(p<5/6\).
Use the following rate-increasing moves on (3).

First decrease any \(s>1/2\) to \(1/2\). This is valid
because \(\partial_sE_\lambda=\lambda'(s)+J'(s+t)\le0\)
by (4) and \(J'\le\log2\). Next decrease \(q>.42\)
to \(.42\), \(t>.5\) to \(.5\), and
\(.5<p<5/6\) to \(.5\). The last three derivative
inequalities are exactly those of
[outer-index elimination](research_mixed_contracted_pair_outer_index_elimination.md),
Section 5: the incoming cap term has no \(t,p,q\) derivatives.
All four coordinates now lie in
\([0,.5]^3\times[0,.42]\).

For \(0<t\le.22<1/4\),
\[
 e^{\partial_tE_\lambda}
 =\{\cos\pi s+\cot\pi t\sin\pi s\}
  \{\cos\pi p+\cot\pi t\sin\pi p\}\ge1.
 \tag{17}
\]
Thus raise low \(t\) to \(.22\). Decrease any
\(p>.42\) to \(.42\), using the unchanged
\(e^{\partial_pE}<500/729\) barrier. Raise low
\(p\) to \(.2\) by the direct sine-ratio proof in
[enlarged tail reduction](research_mixed_contracted_pair_enlarged_tail_reduction.md),
Section 2; its hypothesis \(t\ge.2\) is satisfied.
Then raise low \(q\) to \(.2\) by the original low-\(q\)
barrier. These moves preserve all three supports. No extra
high-\(t\) clip to \(.45\) is imposed.

It remains to place \(s\) in \([.27,.49]\).
If \(0<s\le.27\), then \(.22<s+t\le.77\), so
\(J'(s+t)>0\), while (4) gives
\(\lambda'(s)>27/50\). Raise \(s\) to \(.27\).
If \(.49\le s\le.5\), then \(.71\le s+t\le1\).
On this interval \(J'(s+t)<3/5\). For an elementary
bound, \(\sin(\pi(s+t))\le\sin(.29\pi)<\sin1<101/120\),
and \(101/60<1+3/5+(3/5)^2/2+(3/5)^3/6<e^{3/5}\).
Equation (4) therefore gives \(\partial_sE_\lambda<0\)
on \([.49,.5)\); the endpoint follows by continuity.
Decrease \(s\) to \(.49\).

Every move preserves or increases the rate. A coordinate initially
outside the central interval stops at its boundary, or first at a
point still outside it and later at that boundary. No subsequent
move removes that marker. Thus the final point lies on
\(\partial C_{\mathrm{cap}}\), not merely in its interior.
All singular coordinate endpoints in these moves are handled by
continuity of the real rates, not by evaluating their logarithmic
derivatives there.

On \(C_{\mathrm{cap}}\), (3) is exactly
\(\Re\mathcal F_{\mathrm{cap}}\) at zero index heights.
Proposition 2 of the prepared-cap source theorem proves strict
joint concavity on this full box. Its restriction to each of the
eight faces is therefore strictly concave.

**Theorem.** The complete physical tail of the exact prepared-cap
source, outside the interior of (16), has upper exponential rate
\[
 \boxed{\quad
 \max\left\{\frac{146}{75},
              \max_{u\in\partial C_{\mathrm{cap}}}E_\lambda(u)
                                                \right\}.\quad}
 \tag{18}
\]
More precisely every fixed ordinary jet has a polynomial prefactor
and any prescribed additional positive rate tolerance in this bound.
For each such tolerance, it also holds on sufficiently small fixed
ordinary-color and Fourier-output neighborhoods of \((-2,x_0)\).

*Proof.* Use (11) and (13) for the two true endpoint strips,
(2)--(3) on the fixed compact middle, (15) for its far-\(p\)
part, and the tail-preserving clips for what remains. Both endpoint
ceilings are smaller than \(146/75\). The at most \(N^4\)
physical rows cost only a polynomial. Uniform zero-safe products
and the actual coefficient theorem provide the stated tolerances
and fixed-jet bounds. Their compact-parameter continuity, with the
literal Newton regularization at the endpoints, gives the small
parameter neighborhoods. \(\square\)

Equation (18) does not compare its right side with a critical
action. In particular no face values or signs have been evaluated,
and an original prepared critical point at \(y=x_0\) has not
been identified. The outer index aliases and joining currents
also remain separate. The new conclusion is a complete coherent
physical-tail reduction with true endpoints retained, rather than
reuse of the paired kernel's already certified phase comparisons.
