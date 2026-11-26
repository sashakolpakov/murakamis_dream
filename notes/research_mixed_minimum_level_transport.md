# Raising the smallest coordinates on the coupled contour

Research note, 4 November 2026. The argument below reduces a phase
comparison for arbitrarily long cyclic words to a local derivative
inequality. The implication is proved here. Its derivative hypothesis
has not yet been established for every required configuration, so this
note does not assert an unconditional new bound for the original finite
sum. Section 5 explains the finite-sum consequence once that local
inequality is established.

The useful path moves all coordinates that attain the current minimum
together. Moving just one coordinate need not increase the phase. In
particular, numerical tests of separate coordinate monotonicity cannot
justify the argument below.

## 1. Phase, contour and derivative hypothesis

Fix a cyclic word of length \(m\ge1\), with each position of type three
or four. Let \(r=(r_1,\ldots,r_m)\) be its original complex critical
point, and write
\[
 a_j=\Re r_j,\qquad c_j=\Im r_j.
\]
The known reference bounds give \(a_j\ge .27\) and
\(a_j\in[.22,.45]\). Define
\[
 b=\frac1{10},\qquad \ell=\frac{11}{50},\qquad
 u=\frac9{20},\qquad s=\frac{25}{3},
\]
and, on the interval used in this note, put
\[
 \rho(t)=
 \begin{cases}
 s(t-b),&b\le t\le\ell,\\
 1,&\ell\le t\le u.
 \end{cases}                                                    \tag{1}
\]
For a real vector \(x\in[b,u]^m\), the unselected contour is
\[
 H_j(x)=c_j\min\{\rho(x_{j-1}),\rho(x_j),\rho(x_{j+1})\},
 \qquad z_j(x)=x_j+iH_j(x).                                    \tag{2}
\]
This is the restriction of the
[minimum-neighbor contour](research_mixed_minimum_neighbor_contour.md).
Cyclic subscripts may coincide when \(m=1\) or \(m=2\).

Write the original allocated phase as
\[
 \Phi(z)=\sum_{j=1}^m\phi_j(z_j,z_{j+1}),\qquad
 G_j(z)=\frac{\partial\Phi}{\partial z_j}(z),\qquad
 F(x)=\Re\Phi(z(x)).                                          \tag{3}
\]
Here \(\phi_j\) is the two-variable critical phase of the original
block, including its allocated factorial weights. In particular
\[
 G_j=\partial_2\phi_{j-1}+\partial_1\phi_j.                    \tag{4}
\]
Both incidences in (4) are retained, including for a one-vertex loop.
The closed cotangent root theorem makes these phases holomorphic on a
neighborhood of all the compact parameter sets in use.

For a position \(i\) attaining the minimum of \(x\), define the real
quantity
\[
 D_i(x)=\Re G_i(z(x))+
   \sum_{j\in(i-1,i,i+1)}
      \min\{-s c_j\Im G_j(z(x)),0\}.                          \tag{5}
\]
The sum in (5) has three terms, with multiplicity. It is deliberately
conservative when cyclic subscripts repeat.

The local hypothesis needed below is that a constant \(\gamma\ge0\)
satisfies
\[
 D_i(x)\ge\gamma                                               \tag{6}
\]
for every \(x\in[b,u]^m\) with
\(x_i=\min_j x_j<\ell\). A proof uniform over the possible local
types and parameter values would establish (6) for every word length.
Bounded numerical tests are evidence for this hypothesis, not its proof.

## 2. An inequality for the whole path

**Proposition 1.** Suppose (6) holds. Set
\(x_j^\uparrow=\max\{x_j,\ell\}\). Then
\[
 F(x)\le F(x^\uparrow)
          -\gamma\sum_{j=1}^m(\ell-x_j)_+,                    \tag{7}
\]
where \((v)_+=\max\{v,0\}\).

**Proof.** There is nothing to prove if every coordinate is at least
\(\ell\). Otherwise, put \(t_0=\min_jx_j\), and consider
\[
 x_j(t)=\max\{x_j,t\},\qquad t_0\le t\le\ell.
\]
Except at finitely many values of \(t\), the moving coordinates are
exactly the set
\[
 S(t)=\{j:x_j<t\}.
\]
They all attain the current minimum \(t\). Let \(N(S)\) be the set
of distinct positions whose three-position neighborhood meets \(S\).
Because \(\rho\) is nondecreasing on \([b,u]\),
\[
 \min_{k\in(j-1,j,j+1)}\rho(\max\{x_k,t\})
 =\max\left\{\min_{k\in(j-1,j,j+1)}\rho(x_k),\rho(t)\right\}.
                                                                    \tag{8}
\]
Consequently, almost everywhere along the path,
\[
 \frac{d x_j(t)}{dt}=\mathbf1_{j\in S(t)},\qquad
 \frac{d H_j(x(t))}{dt}=s c_j\mathbf1_{j\in N(S(t))}.
\]
The ordinary chain rule therefore gives
\[
 \frac{d}{dt}F(x(t))
 =\sum_{i\in S(t)}\Re G_i
       +\sum_{j\in N(S(t))}p_j,
 \qquad p_j=-s c_j\Im G_j.                                   \tag{9}
\]
All gradients in (9) are evaluated at \(z(x(t))\).

For \(j\in N(S)\), let \(n_j\ge1\) count its occurrences in the
three-term neighborhoods of positions in \(S\), retaining cyclic
multiplicity. Then
\[
 \sum_{i\in S}D_i
 =\sum_{i\in S}\Re G_i+\sum_{j\in N(S)}n_j\min\{p_j,0\}
 \le\sum_{i\in S}\Re G_i+\sum_{j\in N(S)}p_j.                \tag{10}
\]
Indeed, a negative height contribution can be counted several times
on the left, and a positive one is omitted. Combining (6), (9) and
(10) yields \(dF(x(t))/dt\ge\gamma|S(t)|\) almost everywhere.

The contour is Lipschitz and the phase is smooth on the relevant
compact set, so the function of \(t\) is absolutely continuous.
Integration is legitimate even when the minimum changes hands or
several coordinates move together. Finally,
\[
 \int_{t_0}^{\ell}|S(t)|\,dt
      =\sum_j(\ell-x_j)_+.
\]
This proves (7). The use of distinct positions in (9) and multiplicity
in (10) also proves the statement for cycles of length one and two.
\(\square\)

## 3. Why nonnegativity is enough for a strict phase loss

On the plateau, \(H(x)=c\), so write
\[
 f_c(y)=\Re\Phi(y+ic),\qquad y\in[\ell,u]^m,
 \qquad M=\Re\Phi(r).
\]
The existing fixed-height phase theorem gives a constant \(\mu>0\)
such that
\[
 -D^2f_c(y)\succeq\mu I.                                     \tag{11}
\]
One can choose \(\mu\) independently of word length: take a positive
lower eigenvalue bound for each of the four local block Hessians on
its compact typed plateau domain, then sum the block quadratic forms.
Each coordinate occurs twice, also for loops and repeated incidences.
Compactness supplies a positive local bound because the closed
cotangent theorem gives strict positive definiteness everywhere on
these domains. No numerical value of \(\mu\) is required here.

Since \(\nabla\Phi(r)=0\), the point \(a=\Re r\) is stationary
for \(f_c\). Taylor's formula along the real segment from \(a\)
to \(y\) gives
\[
 f_c(y)\le M-\frac\mu2\|y-a\|_2^2.                           \tag{12}
\]
If at least one original coordinate satisfies \(x_j\le\ell\),
then \(x_j^\uparrow=\ell\), whereas \(a_j\ge .27\). Thus
\(\|x^\uparrow-a\|_2^2\ge(.05)^2=1/400\).

**Corollary 2.** If (6) holds with \(\gamma\ge0\), every
\(x\in[b,u]^m\) with at least one coordinate at most \(\ell\)
satisfies
\[
 F(x)\le M-\frac\mu{800}
               -\gamma\sum_j(\ell-x_j)_+.                    \tag{13}
\]
In particular, proving \(D_i\ge0\) is enough for a strict uniform
phase loss. A larger positive constant is useful but unnecessary.

## 4. Splitting the local inequality into two overlapping pieces

The hypothesis (6) involves neighboring gradients and cannot be
replaced by a bound for \(\Re G_i\) alone. The following exact
decomposition is useful for checking it.

Fix any real number \(\kappa\), and put
\[
 P_i=\partial_2\phi_{i-1}+i\kappa,\qquad
 Q_i=\partial_1\phi_i-i\kappa.
\]
Then \(P_i+Q_i=G_i\). For \(\chi\in\{0,1\}\), define
\[
 \begin{split}
 L_i(\chi)&=\Re\{(1+i\chi s c_i)P_i\}
                   +\min\{-s c_{i-1}\Im G_{i-1},0\},\\
 R_i(\chi)&=\Re\{(1+i\chi s c_i)Q_i\}
                   +\min\{-s c_{i+1}\Im G_{i+1},0\}.
 \end{split}                                                   \tag{14}
\]
The same switch \(\chi\) and the same center height \(c_i\) occur
in both expressions. Direct addition gives the identity
\[
 D_i=\min_{\chi\in\{0,1\}}\{L_i(\chi)+R_i(\chi)\}.          \tag{15}
\]
The two added imaginary constants cancel exactly. They are only an
algebraic device for distributing the derivative between the two
pieces; they do not change a block, a boundary factor, or the original
finite invariant. Uniform lower bounds for both pieces, valid for both
values of \(\chi\), therefore imply (6). This reduction still has
to respect all possible neighboring minima and the actual typed
height intervals.

## 5. The corresponding implication for the finite integral

The finite-sum input is now supplied by
[the adjacent-transition source theorem](research_mixed_transition_pair_source.md),
Corollary 2. For each ordered pair of types, it gives the complete
conditional asymptotic on an open neighborhood of the independent
polygon product containing every pair of targets in (2). This includes
the cases where both arguments are in the transition region. The
action, normalization and nonzero coefficient are those of the original
finite function; all its endpoint terms and remainder integrals are
included in that theorem.

The unselected outer Fourier weights have the correct upper rate on
this whole domain. Indeed, at a type-four target \(z=x+ih\) here,
\(.1\le x\le.45\) and \(h\le0\). Put
\(r=e^{2\pi h}\) and \(\theta=-2\pi x\). For \(0<t\le r\le1\),
\(\Arg(1-te^{i\theta})>0\), since \(-\pi<\theta<0\). Thus
\[
 \Im\operatorname{Li}_2(re^{i\theta})
   =-\int_0^r\Arg(1-te^{i\theta})\,\frac{dt}{t}<0,
 \qquad \Re g(z)<0.                                          \tag{16}
\]
By compactness, \(-\Re g\) has a positive lower bound on these
type-four targets. The true Fourier-polynomial bound therefore has
upper rate \(-\Re g(z)+\varepsilon\), for any fixed
\(\varepsilon>0\); its forcing alternative has rate zero. This
argument uses the complete upper bound, not a replacement of the
polynomial by its values at roots of unity.

Let \(\mathcal I_{N,\varnothing}(E)\) denote the contribution from a
real parameter set \(E\) to the exact normalized unselected integral
on (2), with its original scalar and level powers. Put
\(X=[.1,.45]^m\) and \(P=[.22,.45]\).

**Corollary 3.** Suppose (6) holds with \(\gamma\ge0\). For each
fixed cyclic word there are constants \(C,A\) such that
\[
 \left|\mathcal I_{N,\varnothing}(X)
       -\mathcal I_{N,\varnothing}(P^m)\right|
       \le C N^A\exp\{N(M-\mu/1600)\}                       \tag{17}
\]
for all sufficiently large integer levels. Consequently the restricted
unselected integral on \(X\) retains the original nonzero central
coefficient and its level power \(N^0\), at both parities.

**Proof.** The source theorem just cited bounds each complete
conditional factor uniformly by a fixed polynomial in \(N\) times
its critical exponential. Combining these with (16) and the original
integer Fourier weights gives rate at most \(F(x)+m\varepsilon\).
Choose \(\varepsilon<\mu/(1600m)\). On \(X\setminus P^m\),
Corollary 2 gives \(F(x)\le M-\mu/800\). The contour Jacobian is
bounded by \((38/25)^m\), and the real domain has bounded measure.
All factors outside the exponential have at most polynomial growth
for a fixed word. This proves (17).

On \(P^m\), the contour has the fixed original heights and Jacobian
one, and its central asymptotic is already proved. Its nonzero
coefficient makes (17) exponentially smaller than that leading term.
The exact normalization is the same on both regions, so no new power
of \(N\) or scalar is introduced. \(\square\)

Proposition 1 and its corollaries remain conditional on the explicit
local derivative hypothesis (6). The complete source packet is now an
established input; the derivative certificate is still pending.
These assertions concern unselected coordinates in \([.1,.45]^m\).
They do not treat selected heights, configurations also containing low
or right-half coordinates, or the open boundary parameters needed for
knot assembly.
