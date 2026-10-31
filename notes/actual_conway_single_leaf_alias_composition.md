# A single-leaf alias gap that composes with an arbitrary completed child

31 October 2026. source-envelope theorem. The proof
retains the actual seven-factorial multiplication gate and the completed
child's output tangent. It uses no child coefficient lower asymptotic or
replacement coupon. The [finite source and lattice adapter](actual_conway_single_leaf_source_composition.md)
and [geometric proper-port theorem](actual_conway_single_leaf_geometric_composition.md)
are separate inputs. The applicable closed class has two completed root
children and proper completed ports $0<X,Y<1$. Root-leaf closures that
reach the quarter-index equal-modulus dominance boundary remain separate.

## 1. Exact parameter domain at a single-leaf attachment

Attach the original leaf $h$ to a completed child $E$ by the original
product. The selected common $X$ is the cotangent of the leaf coordinate
$a$. Write the child port as $(B,X,Y)$, its output as
$(B_p,X,Y_p)$, and the corresponding output angles as $b,c$.
Original product stationarity gives

\[
\begin{aligned}
a&=\frac{\operatorname{arccot}X}{\pi},&
b&=\frac{\operatorname{arccot}B}{\pi},&
c&=\frac{\operatorname{arccot}B_p}{\pi},\\
Y^2&=1+B^2-X^2,&S&=X+B>0,\\
B_p&=X-\frac1S,&Y_p&=\frac YS,\\
\mu&=P_E'(b)=2\log(X/Y),&
\lambda&=P_{\mathrm{parent}}'(c)=2\log(X/Y_p).
\end{aligned}\tag{1}
\]

Here $\operatorname{arccot}$ takes values in $(0,\pi)$. Assume both
child and parent are proper: $0<X<1$ and $0<Y,Y_p<1$.
Then $Y<1$ gives $|B|<X$, while $Y_p<1$ is equivalent to

\[
 B>L(X):=\frac1{2X}-X.
\]

Since $B<X$, this forces $X>1/2$. Every newly attached leaf in this
class therefore remains in the strict source interval

\[
 \frac14<a<\frac{\arctan(2)}\pi.\tag{2}
\]

The only region not covered by the earlier individual-leaf certificate
is $1/2<X<2/3$. On its closed enlargement $1/2\le X\le2/3$,

\[
 0<L(X)\le B\le X,\qquad \frac1{2X}\le Y\le1.
\]

The exact reflection $B'=1/(X+B)-X$ maps $[L(X),X]$ onto itself,
interchanges its endpoints, and satisfies $Y_p^2=1+(B')^2-X^2$.
Consequently, setting $p=e^\mu$ and $q=e^\lambda$,

\[
 p,q\in[X^2,4X^4]\subset[1/4,1],\qquad
 \mu,\lambda\in[-2\log2,0].\tag{3}
\]

This compact slope domain follows from actual proper ports; it is not
an extra assumption on the source.

## 2. A universal dual inequality with a linear child

Retain the [original complete, core and alias actions](actual_conway_uniform_two_leaf_block_alias_gap.md):

\[
\begin{aligned}
J(t)&=\int_0^t\log(2\sin(\pi u))\,du,&
g(t)&=J(2t)-4J(t),\\
\widetilde g(t)&=g(\max(t,1/4)),&k(t)&=-2J(t/2),\\
m(x,y,z)&=J(x+y)+J(z)-J(x)-J(y)\\
&\quad-J(z-x)-J(z-y)-J(x+y-z),\\
D&=\{x,y\ge0:\max(x,y)\le z\le x+y\le1\}.
\end{aligned}
\]

Define

\[
\begin{aligned}
P(\mu,\lambda)
 &=\max_{D,\,x\le1/2}
       [g(x)+m(x,y,z)+\mu y-\lambda z],\\
Q(\mu,\lambda)
 &=\max_D[k(x)+m(x,y,z)+\mu y-\lambda z].
\end{aligned}\tag{4}
\]

Only the new leaf has the core restriction $x\le1/2$ in $P$.
The completed child coordinate $y$ retains its full interval $[0,1]$:
it is bounded by its own tangent, not identified with another bare leaf.

There is an exact calibration on the whole square (3). Set

\[
\begin{aligned}
X&=\sqrt{p+q+pq}-\sqrt{pq},&S&=\sqrt{q/p},\\
B&=S-X,&B_p&=X-1/S,\\
a&=\operatorname{arccot}(X)/\pi,&
b&=\operatorname{arccot}(B)/\pi,&
c&=\operatorname{arccot}(B_p)/\pi.
\end{aligned}\tag{5}
\]

Here $1/2\le X<1$. Indeed $X\ge1/2$ is equivalent to
$p+q-\sqrt{pq}\ge1/4$, which follows from
$(\sqrt p-\sqrt q)^2+\sqrt{pq}\ge1/4$.
And $X<1$ follows from $(\sqrt p-\sqrt q)^2<1$.
Also $Y^2=1+B^2-X^2=X^2/p>0$. The point $(a,b,c)$ is strictly
in $D$: $X+B=S>0$, $X-B_p=1/S>0$, $B-B_p=Y^2/S>0$,
and the remaining sine numerator is $X^2>0$. The actual derivatives are

\[
 m_x(a,b,c)=-2\log X,\qquad m_y(a,b,c)=-\mu,\qquad
 m_z(a,b,c)=\lambda.\tag{6}
\]

Since $g'(a)=2\log X$, global concavity proves

\[
 P(\mu,\lambda)=g(a)+m(a,b,c)+\mu b-\lambda c.\tag{7}
\]

**Square certificate.** On the full square in (3),

\[
 Q(\mu,\lambda)\le P(\mu,\lambda)-\frac1{1000}.
 \tag{8}
\]

The [exact verifier](../experiments/verify_conway_single_leaf_attachment_certificate.py)
and [rational data](../experiments/conway_single_leaf_attachment_certificate.json)
partition the entire square into 55 dyadic rectangles. On each rectangle,
a fixed feasible rational pure point gives a lower bound for $P$.
A fixed rational tangent to the concave function $k+m$ gives a global
upper bound for the alias action. The four exact vertices of $D$ are

\[
 (0,0,0),\quad(1,0,1),\quad(0,1,1),\quad(1/2,1/2,1/2).
\]

Together with the four slope corners, these give 16 inequalities per
rectangle, or 880 in total. Affinity covers every rectangle and the
entire product polytope. Recursive subdivision proves coverage without
gaps. The [result record](../experiments/conway_single_leaf_attachment_certificate_results.json)
has minimum certified lower bound

\[
 \frac{55437191760019874892517972684020763373}{10^{40}}
 >\frac1{1000}.
\]

The verifier uses the same rational engine as the two-leaf certificate. Its outward arithmetic and sine, logarithm, Machin and integrated Euler-product remainders are explicit there. No optimizer is called, and candidate-state accuracy is not a premise.

## 3. The actual new-leaf inequality and inherited gap

Let $C=P_E(b)$ be the child's selected complete value. Suppose its core
and aggregate alias arrays satisfy, uniformly in all physical colors and
all output indices $r$,

\[
\begin{aligned}
 |C_{E,r}|&\le\exp\!\left(N[C+\mu(r/N-b)+e_N]\right),\\
 |A_{E,r}|&\le\exp\!\left(N[C+\mu(r/N-b)-\gamma_E+e_N]\right),\\
 e_N&\longrightarrow0,\qquad\gamma_E>0.
\end{aligned}\tag{9}
\]

This is an output-tangent upper bound. It does not say that the same
weights minimize a separate constrained problem at every $r$.

For an alias at the new leaf, adding the child tangent gives its constant
$C-\mu b$ plus $k(x)+m+\mu y$. Equations (7)–(8) prove

\[
\begin{aligned}
 k(x)+m(x,y,z)+C+\mu(y-b)
 &\le P_{\mathrm{parent}}(c)+\lambda(z-c)-\frac1{1000},\\
 P_{\mathrm{parent}}(c)&=g(a)+C+m(a,b,c),
 \qquad 1/2<X\le2/3.
\end{aligned}\tag{10}
\]

This is the original parent action and slope, with its actual boundary
coordinate. For $X\ge2/3$, the
[earlier exact algebraic leaf certificate](actual_conway_algebraic_leaf_alias_certificate.md)
gives

\[
 k(x)\le g(a)+g'(a)(x-a)-\frac1{2500}.
\]

The original gate and child tangents cancel the $x,y$ terms by (6).
Thus the same block inequality holds for every proper attachment with
uniform margin

\[
 \delta_{\mathrm{leaf}}=\frac1{2500}.\tag{11}
\]

For a new core leaf, $\widetilde g$ is bounded by its complete tangent
because $a>1/4$. The same calculation gives the parent tangent with
zero loss.

The exact finite parent split is

\[
\begin{aligned}
 C_{\mathrm{parent}}&=C_h\star C_E,\\
 A_{\mathrm{parent}}&=A_h\star C_E+C_h\star A_E+A_h\star A_E.
\end{aligned}\tag{12}
\]

Here $\star$ is the original Newton kernel, including $i+j\le d=N-1$
and all normal directions. The three terms lose, respectively,
$\delta_{\mathrm{leaf}}$, $\gamma_E$, and their sum. Polynomially
many kernel indices and the uniform $O(\log N)$ factorial errors can
be absorbed into a new error tending to zero. Hence (9) propagates with

\[
 \gamma_{\mathrm{parent}}
     =\min(\gamma_E,\delta_{\mathrm{leaf}})>0.\tag{13}
\]

The order $Eh$ gives the same statement by the exact commutative product;
no coupon is moved through a turn.

Turns and completed/completed products preserve the tangent hypotheses.
The actual turn reverses $r$ to $d-r$, changes the slope from $\mu$
to $-\mu$, and has finite affine error $-\mu/N$. A product of two
completed children uses their two tangent bounds and the actual gate
tangent; internal derivatives cancel, and a contaminated sector retains
at least its smaller child margin. This proves a finite-tree induction,
including $hT(E)$ when $T(E)$ is a proper completed child. The closing
demand and all turns still use $d/N=1-1/N$, so their total finite
error is $O(1)$ in the exponent for a fixed tree.

The two-leaf block lemma supplies the $A_2$ base. Larger
original seeds may use their earlier leaf proof or the proved composition
where proper. Every nonempty alias sector in a proper completed/completed
closure therefore has a positive global gap. The all-core concave
majorant and actual far-color recurrence give the physical-color
complement. The strict-state, high-leaf and primitive-lattice hypotheses
are checked in the linked source and geometry companions; they are not
inferred from this upper bound.

## 4. A stronger response bound on actual proper ports

The square certificate does not depend on this section. The following
separate argument shows that, for $1/2\le X\le2/3$, the dual gap is
at least its value at $\mu=\lambda=-\log4$. A four-vertex certificate
then gives the stronger margin $3/50$ on this smaller parameter set.

Fix $p,q>0$ and optimize $m+\mu y-\lambda z$ over $y,z$ at a fixed
$0<x<1$. Each fiber has strict points. Every saturated gate constraint
has a nonvertex-flat original tetrahedron, so motion toward a strict
point has positive infinite inward derivative; the linear terms remain
finite. The gate maximum is strict. Its Hessian in $y,z$ is negative
definite: the first angle triple controls $y$, and with $y$ fixed the
second controls $z$. The fiber maximum is unique and analytic in $x$,
and its partial Legendre profile is concave.

Write

\[
 U=\cot(\pi x),\quad V=\cot(\pi y),\quad W=\cot(\pi z),\qquad
 A=U-W>0,\quad r=q/p,\quad c_0=\frac{q(p+q+1)}p.
\]

Using the original signs $m_y=-\mu$, $m_z=\lambda$,

\[
 U+V=rA,\qquad V=rA-U,\qquad
 c_0A^2-2qUA-(1+U^2)=0,\qquad E=c_0A-qU>0.
 \tag{14}
\]

The positive quadratic root is the unique strict physical fiber.
Implicit differentiation gives exactly

\[
 \frac{dW}{dU}=\frac{(1+q)V}{E},\qquad
 \frac{dV}{dU}=\frac{(q/p)(1+p)W}{E}.\tag{15}
\]

At the pure state of an actual port with $X\le2/3$, one has
$V=B>0$ and $W=B_p<0$. Increasing $x$ lowers $U$, so (15)
strictly increases $V$ and decreases $W$. Those signs are preserved
through continuation toward $x=1$. The optimized child angle $y$
therefore decreases and output angle $z$ increases.

At the pure $a$, the alias action $k(x)$ plus this partial Legendre
profile has derivative $k'(a)-g'(a)>0$. This strict inequality holds
on $[1/4,1/2)$, as proved in the
[monotone two-leaf response theorem](actual_conway_two_leaf_monotone_alias_response.md).
Concavity forces its maximizing $x_*$ to exceed $a$. The possible
endpoint $x_*=1$ has uniquely $y_*=0,z_*=1$ and satisfies the same
strict comparisons. Strict concavity of $k$ makes the complete alias
maximizer unique; Danskin differentiation remains valid at that endpoint.
For $\Delta=P-Q$,

\[
 \partial_\mu\Delta=b-y_*>0,\qquad
 \partial_\lambda\Delta=z_*-c>0,
 \quad a\ge1/4,\ V>0,\ W<0.
 \tag{16}
\]

A parameter path stays in this regime. At an actual port with $X\le2/3$,
$p,q\ge1/4$. If $p\ge q$, first run $(t,t)$ from $t=1/4$ to $q$,
then $(p',q)$ from $p'=q$ to $p$. On the diagonal,
$X=\sqrt{t^2+2t}-t$ increases, $V=1-X>0$, and $W=X-1<0$.
On the second piece $X_p>0$, because $p'(1+q)>q^2$. Thus $X$
stays between $1/2$ and its actual terminal value, at most $2/3$.
There $S=\sqrt{q/p'}\le1$ implies $W=X-1/S<0$; and $V=S-X$
decreases to its positive final value, so remains positive.

Both logarithmic slopes increase along this path. If $p\le q$, use

\[
 m(x,y,z)=m(x,1-z,1-y).
\]

This exact gate involution swaps $\mu,\lambda$ and adds the same
constant to both dual values. It preserves $\Delta$ and supplies
the symmetric path. Equation (16) proves

\[
 \Delta(\mu,\lambda)\ge\Delta(-\log4,-\log4).
 \tag{17}
\]

The limiting $X=1/2$ endpoint is included. No alias branch was selected
by squaring a stationary equation.

The [endpoint verifier](../experiments/verify_conway_single_leaf_endpoint_certificate.py)
uses the same rational engine, with pure point
$(352416,352416,647584)/10^6$ and alias tangent point
$(570352,246081,753919)/10^6$. At $\mu=\lambda=-2\log2$ it checks
all four vertices of $D$. The [exact result](../experiments/conway_single_leaf_endpoint_certificate_results.json)
has minimum lower bound

\[
 \frac{613089614904949907163494204377649845509}{10^{40}}
 >\frac3{50}.
 \tag{18}
\]

The feasible pure point bounds $P$ below, and the global $k+m$
tangent bounds $Q$ above. Optimizer accuracy is not a premise. Together
with (17), this proves the stronger actual-port margin stated here.

## 5. Scope and the root-leaf frontier

This is an upper-envelope induction at a selected proper completed-port
configuration of the original source. The source and geometry companions
supply such configurations for their stated grammar. No claim is made
that every algebraic tangle has the required strict states or local packet.

In particular $C(hT(A_s))$ is a different boundary regime. Its seed has
$X=1$, $B=Y=1/s$, so every inner leaf label equals $1/4$, whereas
the outer leaf has cotangent $1/s$. Its pure retained cells can remain
strict. The inherited signed source packet meets an equal-modulus
dominance boundary there, not an eigenvalue collision or a forced-flat
geometric cell. Equations (11)–(13) do not remove that separate packet
obligation.

## scope and exact verification


The square certificate is the primary proof of the uniform compositional
margin. The response argument and endpoint certificate independently
strengthen it on the actual proper-port subdomain. Neither proof relies
on numerical sampling or a coefficient lower asymptotic.
