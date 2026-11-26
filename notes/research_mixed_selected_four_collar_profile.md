# Selected type-four angle profile at the first collar

Research deduction, 5 November 2026. The selected second type-four
coordinate has the same concave source profile as the unselected one
throughout \([.22,3/8]\), containing the second-coordinate range already
admitted by the horizontal completion theorem. On the rest of the plateau
an explicit two-branch profile remains available. The proof retains the
full Fourier forcing branch and all conditional rows. It uses elementary
inequalities only, with no new roots, parameter cells, or finite-level
sampling.

## 1. The literal selected halfweight

Use \(P=[11/50,9/20]\), \(H=7/500=.014\), and the notation of
[the angle-profile theorem](research_mixed_first_collar_angle_profiles.md).
For \(0\le k\le H\), \(x\in P\), and \(Y=e^{-2\pi i(x+ik)}\),
the source in question is
\[
 |C_{1,N}(1,Y)|\,|d_N(Y)Y^{-N}|^{1/2}.
 \tag{1}
\]
This is the first allocated half of the selected second weight. The
other half remains in the next conditional factor.

Put \(G_k(x)=\Re g(x-ik)<0\). The exact reflection identity for the
original primitive gives
\[
 \Re g(x+ik)=G_k(x)-\pi k(1-2x).
\]
The whole Fourier theorem therefore supplies the selected halfweight
upper rate
\[
 W_+(x,k)=\frac12\max\{-\Re g(x+ik)-2\pi k,0\}
        =B-\min\{A,B\},\quad
 A=\pi k(1/2+x),\quad B=-G_k(x)/2>0.
 \tag{2}
\]
In particular both alternatives remain. This formula is a rate upper
bound for the actual Fourier polynomial, not its replacement by one
homogeneous branch.

Let \(I_k,R_1,S_1\) be the original row integral and profile from the
cited theorem. The radial reciprocal identity
\(I_k(u,x)=2\pi ku+I_{-k}(u,x)\) gives the exact rate relation
\[
 \begin{split}
 F_+(u,x,k)&:=R_1(u,x,k)+W_+(x,k)\\
 &=\underbrace{I_{-k}(u,x)-2J(u)-G_k(x)/2}_{F_-(u,x,k)}
                       +2\pi ku-\min\{A,B\}.
 \end{split}
 \tag{3}
\]
Lemma 1 of that theorem proves \(F_-(u,x,k)\le S_1(x)\) for
every row, since \(-k\ge-.014>-.102\).

## 2. Every upper row is retained

For \(v\in[0,1/2]\), the same Poisson-arc inequality as in the
unselected theorem implies
\[
 F_+(1-v,x,k)-F_+(v,x,k)
                 \le 2\pi k(1-2v)+2J(v).
 \tag{4}
\]
The Fourier halfweight cancels because it is independent of the row.

Take \(d=1/50\). The elementary bound \(2\sin\pi t\le2\pi t\)
gives
\[
 J(d)\le d\{\log(2\pi d)-1\}<-7/150
                         <-2\pi H(1/2-d).
 \tag{5}
\]
Indeed \(2\pi d=\pi/25<1/4\) and
\(\log4>4/3\). The last inequality follows already from
\(\pi<22/7\). Convexity of \(J\) on \([d,1/2]\), together
with \(J(1/2)=0\), now gives
\(J(v)\le-2\pi H(1/2-v)\) throughout that interval.
Consequently the right side of (4) is nonpositive when \(v\ge d\).
All these upper rows are bounded by their reflected lower rows.

For the remaining last rows, \(0\le v\le d\), Jensen's identity
and the minimum arc integral give
\(I_{-k}(1-v,x)\le-2J(v/2)\). Hence
\[
 R_1(1-v,x,k)
 \le2\pi k(1-v)+2\{J(v)-J(v/2)\}\le2\pi H,
 \tag{6}
\]
because \(J\) decreases on \([0,d]\).
The literal polynomial maximum-modulus bound from the
[whole seam source](research_mixed_boundary_strip_bounds.md)
gives the selected halfweight upper rate at most \(1/12\).
Equivalently, apply its inside-unit-circle bound to
\(Y^{-N}d_N(Y)\) on the exterior. Thus this entire last-row
piece has rate at most \(2\pi H+1/12\).
The explicit rate (2) has the same bound: its factorial alternative
has height derivative \(\Im g'(x+ik)/2-\pi<0\), and its
forced alternative is zero. Hence
\(W_+(x,k)\le-J(x)/2<1/12\).

On the other hand the quarter-row trial from the unselected profile
proof gives \(S_1(x)>1063/4950\): the extra terms
\(-J(1/4)-J(x)/2\) compared with the type-three trial are positive.
Therefore
\[
                2\pi H+1/12<1063/4950<S_1(x).
 \tag{7}
\]
The inequalities extend through \(k=0\) by continuity of the row
integrals. They include wrapped rows and physical zeros; no upper
row is deleted by a terminating identity.

## 3. The selected halfweight pays the lower-row height change

For \(u\in[13/50,1/2]\),
\[
 \partial_uR_1
 =\log|1-e^{2\pi k-2\pi i(x+u)}|-2\log(2\sin\pi u)<0.
\]
Indeed \(e^{2\pi H}<11/10\), whereas
\(4\sin^2(13\pi/50)=2+2\sin(\pi/50)>21/10\).
For example \(2\pi H<.088\) and
\(e^t\le(1-t)^{-1}\) imply the first bound. For the second,
\(3/50<\pi/50<1/10\) and
\(\sin t\ge t-t^3/6>1/20\).
Every lower-half maximum is therefore at a row \(u\le13/50\).

On such rows, (3) gives an excess above \(S_1(x)\) of at most
\((13/25)\pi k-\min\{A,B\}\).
The choice \(A\) is always favorable because
\(1/2+x\ge.72>13/25\). For the choice \(B\), retain
the original logarithm:
\[
 \partial_kG_k(x)=\Im g'(x-ik)\le\pi(1/2-x).
\]
For fixed \(x\), the argument of \(1-Re^{-2\pi ix}\) increases
with \(0<R\le1\), so its value is at most its unit-radius
value \(\pi(1/2-x)\). Thus
\(G_k(x)\le J(x)+\pi k(1/2-x)\). It follows that
\[
 \max_u F_+(u,x,k)
 \le S_1(x)+D_H(x),\qquad
 D_H(x)=\left[\pi H\left(\frac{77}{100}-\frac x2\right)
                                      +\frac{J(x)}2\right]_+.
 \tag{8}
\]
The upper rows treated in Section 2 have already been included in
this maximum. The positive part is needed because the other Fourier
branch may be active.

In particular \(D_H(x)=0\) on \([.22,3/8]\).
On this interval \(J(x)\le J(3/8)<-1/16\): the logarithm
\(\log(2\sin\pi t)\) is greater than \(1/2\) throughout
\([3/8,1/2]\), since \(2+\sqrt2>3>e\).
Also
\[
 \pi H\left(\frac{77}{100}-\frac x2\right)
                  \le\frac{66}{100}\pi H<\frac1{32}.
 \tag{9}
\]
Together these make the expression inside the positive part negative.

All numerical comparisons in (5), (7), and (9) follow from the displayed
rational constants and \(\pi<22/7\); no sampled row estimate is involved.

## 4. The finite collar and the completion criterion

**Theorem 1.** For every prescribed \(\eta>0\), uniformly in
\(x\in P\), \(0\le k\le H\), both level parities, and sufficiently
large \(N\), the literal source (1) obeys
\[
 |C_{1,N}(1,Y)|\,|d_N(Y)Y^{-N}|^{1/2}
       \le C_\eta N^A e^{N\{S_1(x)+D_H(x)+\eta\}}.
 \tag{10}
\]
On \(x\in[.22,3/8]\), its rate is simply \(S_1(x)+\eta\).

*Proof.* Apply the uniform zero-safe finite-product upper bounds to
every row and the actual full Fourier upper bound to (2).
Sections 2--3 bound their entire compact row supremum. Add the rows;
their number contributes only a polynomial. The prescribed Fourier
error and all uniform symbol errors are allocated to the one \(\eta\).
No conditional critical point is required at the transported target.
\(\square\)

For a first type \(3+\alpha\), the full first-pair source is now
\[
 |U_{\alpha,N}(w,X)C_{1,N}(X,Y)|
       |d_N(X)^\alpha X^{-N\sigma_1}|
       |d_N(Y)Y^{-N}|^{1/2},
 \quad X=e^{-2\pi ix_1},\quad
 0\le x_1\le\rho\le1/1000.
 \tag{11}
\]
The exact collar bound for \(p_j(X)/P_j\), refined cap ceiling
\(b_\alpha\), and first true Fourier allowance give upper rate
\[
               b_\alpha+C_\alpha(\rho)+S_1(x)+D_H(x)+\eta,
 \tag{12}
\]
using the constants of the unselected angle-profile theorem.
The first selection is \(\sigma_1\in\{0,\alpha\}\); its monomial
still has unit modulus. The cap's fixed ordinary-color neighborhood
and its fixed color derivatives persist.
The neighborhood and collar are chosen before \(N\); zero-safe row
bounds, not pointwise continuity of finite sums, supply uniformity.

On the admitted source domain of the
[horizontal completion theorem](research_mixed_first_collar_horizontal_completion.md),
the second-four real coordinate lies in \((.24,.363)\).
It therefore lies within \([.22,3/8]\), where \(D_H=0\).
The already proved
[type-four finite next-edge transport](research_mixed_four_fixed_contour_transport.md)
retains the other selected halfweight and costs \(13/2000\).
Consequently equation (17) of the angle-profile theorem, with
\(\beta=1\), now applies to **both** second-coordinate selections,
provided its scalar interval \(I\) is chosen inside \([.22,3/8]\).
The first selection remains arbitrary when allowed. There is no
additional selected-row allowance in that criterion.

For an independently justified wider horizontal source domain, the
explicit full-plateau variant replaces \(S_1\) in that criterion by
\[
 \max\left\{S_1(y),\
 S_1(y)+\frac{J(y)}2+
              \pi H\left(\frac{77}{100}-\frac y2\right)\right\}.
 \tag{13}
\]
Each branch is strictly concave: the first was proved in the earlier
note, and \(S_1+J/2\) is the partial maximum of
\(J(y+u)-J(y)-2J(u)=V(y,u)-J(u)\), a jointly strictly concave
function on the same row domain. After subtracting the original
linear force and completion energy, each branch thus has one clipped
scalar maximizer. This reduces the wider selected test to two scalar
candidates; it does not assert its sign or the required wider source
domain.

The actual reference action, remaining tangent, post-pair completion,
safe middle and pinning hypotheses are unchanged. The result removes
an artificial selected-height cost on the already admitted second-four
domain, without proving a whole-boundary or new knot-family theorem.

