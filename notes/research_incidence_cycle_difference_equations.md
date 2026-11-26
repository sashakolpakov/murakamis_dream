# Exact difference equations for the complete incidence sum

Private written deduction, 14 November 2026. This note concerns the
original finite sum, with all phases retained. The additional variables
introduced below record its coefficients; they are not identified with
meridian or longitude eigenvalues.

There are two useful statements. First, alternating cycles in the
event--anchor incidence graph give exact difference equations without
boundary remainders, even at the prescribed root of unity. Second,
these equations determine every coefficient of the finite generating
polynomial from one coefficient. This is rigidity of the coefficient
array. Evaluation of that array can still vanish by cancellation.

## 1. The finite polynomial and its quadratic phase

Let \(G\) be the bipartite multigraph whose vertices are the events
and anchors of the original source. Its edges are their distinct
incidences. Write \(E\) for this edge set and \(C\) for its unsigned
incidence matrix. Parallel edges are retained. Put
\[
 q=e^{\pi i/N},\qquad d=N-1,\qquad
 \mathcal F_d=\{n\in\mathbb Z_{\ge0}^{E}:Cn=d\mathbf1\},
 \qquad S_j=\prod_{r=1}^j2\sin(\pi r/N),\quad S_0=1.
 \tag{1}
\]
Every coordinate of a feasible \(n\) is at most \(d\). We assume
\(\mathcal F_d\ne\varnothing\). The case of empty support gives the
zero polynomial throughout.

Use one event per crossing, together with the original closing
events. The complete source formula and its joint-phase calculation
give, after taking out a specified scalar independent of \(n\),
\[
 w_N(n)=\frac{q^{\Phi_N(n)}}{\prod_{e\in E}S_{n_e}},
 \qquad
 \Phi_N(n)=\frac12 n^{\mathsf T}Hn+Na^{\mathsf T}n+b^{\mathsf T}n.
 \tag{2}
\]
Here \(H\) is a fixed symmetric integral matrix with even diagonal;
\(a,b\) are fixed integral vectors. Their entries come from the
crossing signs, the order of undercrossings, and the closing pivots.
They do not depend on the level. An additive constant in \(\Phi_N\)
belongs to the extracted scalar.

For precision, the joint-phase formula uses linear functions
\(h_j,u_j,v_j,J_j\) of the incidences at each crossing. They are,
respectively, its auxiliary clock, understrand transfer, overstrand
output, and the accumulated understrand input. If \(\alpha_i\)
is the closing index on head \(i\), the complete exponent is
\[
 \Phi_N=
 \sum_j\sigma_j h_j(u_j+2J_j)
 +N\sum_j(h_j-\sigma_jJ_j)
 +\sum_j\sigma_j(h_j+J_j)-2\sum_{i>1}\alpha_i.
 \tag{3}
\]
Thus (2) follows with
\[
 \begin{split}
 H&=\sum_j\sigma_j\{
 h_j\otimes(u_j+2J_j)+(u_j+2J_j)\otimes h_j\},\\
 a&=\sum_j(h_j-\sigma_jJ_j),\\
 b&=\sum_j\sigma_j(h_j+J_j)-2\sum_{i>1}\alpha_i.
 \end{split}
 \tag{4}
\]
In (4), a linear function denotes its integral coefficient vector.
The proof of (3), including its boundary factors, belongs to
[the joint-phase calculation](research_joint_clock_phase_equations.md).
The arguments below also apply to any specified phase of the form (2).

Introduce independent nonzero complex variables \(z_e\), and define
\[
 F_N(z)=\sum_{n\in\mathcal F_d}w_N(n)z^n,
 \qquad z^n=\prod_e z_e^{n_e}.
 \tag{5}
\]
The original scalar is its prescribed external factor times
\(F_N(\mathbf1)\). No normalization by that value is used.
Each coefficient in (5) is nonzero, since \(S_j>0\) for \(0\le j<N\).

Let \(T_e\) act by replacing \(z_e\) with \(qz_e\), fixing the other
variables. These operators commute with one another and satisfy
\(T_ez_e=qz_eT_e\). On a monomial \(z^n\), \(T_e\) has eigenvalue
\(q^{n_e}\). Define
\[
 s(T_e)=\frac{T_e-T_e^{-1}}{i},
 \qquad s(n)=\frac{q^n-q^{-n}}{i}=2\sin(\pi n/N).
 \tag{6}
\]
The conservation equations in (1) give the exact operator identities
\[
 \left(\prod_{e\ni v}T_e-q^d\right)F_N=0
 \quad\hbox{for every event or anchor }v.
 \tag{7}
\]

## 2. Alternating cycles give equations with no boundary remainder

A simple cycle in a bipartite multigraph has even length. Give its
successive edges alternating signs \(+1,-1\), and give all other
edges value zero. Denote the resulting vector by \(c\).
It satisfies \(Cc=0\). A two-edge cycle between parallel incidences
is allowed. Write \(c_+\) and \(c_-\) for its positive and negative
edge sets, and put
\[
 \ell_c=\frac12c^{\mathsf T}Hc+b^{\mathsf T}c\in\mathbb Z.
 \tag{8}
\]

**Theorem 1.** The original generating polynomial satisfies
\[
 \boxed{\left[
 \prod_{e\in c_+}s(T_e)
 -
 z^c(-1)^{a^{\mathsf T}c}q^{\ell_c}
 \left(\prod_eT_e^{(Hc)_e}\right)
 \prod_{e\in c_-}s(T_e)
 \right]F_N=0.}
 \tag{9}
\]
The multiplication by \(z^c\) is on the left of the shift
operators, as displayed. Negative powers are interpreted in the
Laurent polynomial ring.

*Proof.* For \(m,m+c\in\mathcal F_d\), factorial cancellation gives
\[
 \left(\prod_{e\in c_+}s(m_e+1)\right)w_N(m+c)
 =
 q^{\Phi_N(m+c)-\Phi_N(m)}
 \left(\prod_{e\in c_-}s(m_e)\right)w_N(m).
 \tag{10}
\]
The phase difference is exactly
\[
 \Phi_N(m+c)-\Phi_N(m)
 =(Hc)^{\mathsf T}m+Na^{\mathsf T}c+\ell_c.
 \tag{11}
\]
Since \(q^N=-1\), this is the coefficient relation in (9).

It remains to check the boundary of the finite support. On the
left of (9), a term with \(n_e=0\) for any \(e\in c_+\) vanishes
because \(s(0)=0\). Every remaining term has \(m=n-c\ge0\)
and \(Cm=d\mathbf1\), and so has an allowed partner in (10).
On the right, a term with \(m_e=0\) for some \(e\in c_-\)
vanishes for the same reason. Every remaining term has
\(n=m+c\ge0\) and \(Cn=d\mathbf1\).
The row sums ensure all its coordinates are at most \(d\);
there is no additional upper boundary. This pairs every nonzero
term. No value of a sine factorial at \(N\), no division by a
vanishing factor, and no cyclic extension of the index set is
needed. \(\square\)

There are only finitely many simple cycles for a fixed graph, so
(7) and (9) form a finite system whose number of generators does
not grow with \(N\). This is a system in the auxiliary variables
\(z_e\); it is not yet a recurrence in the color or a peripheral
quantum \(A\)-polynomial.

## 3. Rigidity of the finite coefficient array

**Theorem 2.** Among polynomials supported in \(\mathcal F_d\), the
solutions of all the cycle equations (9) form a one-dimensional
complex vector space, spanned by \(F_N\).

*Proof.* First, any two feasible integral flows are joined by
simple alternating cycle moves through feasible integral flows.
To see this, orient every edge of the bipartite graph from its
event to its anchor. For two flows \(n,n'\), the difference
\(n'-n\) has zero signed divergence. Direct its positive entries
with that orientation and its negative entries against it.
At each vertex, total incoming multiplicity equals total outgoing
multiplicity. A nonempty such directed multigraph contains a
directed simple cycle. Its corresponding alternating vector \(c\)
is sign-compatible with \(n'-n\). Thus \(n+c\ge0\), its margins
are unchanged, and its integral distance from \(n'\) is strictly
smaller. Repeating finishes after finitely many moves.

Now let \(G(z)=\sum_{n\in\mathcal F_d}g(n)z^n\) satisfy (9).
For adjacent feasible flows \(m,m+c\), comparison of the coefficient
of \(z^{m+c}\) gives (10) with \(g\) in place of \(w_N\).
All sine factors in that relation lie at indices \(1,\ldots,d\)
and are nonzero. Therefore
\[
 \frac{g(m+c)}{w_N(m+c)}
             =\frac{g(m)}{w_N(m)}.
 \tag{12}
\]
Connectivity makes the ratio constant on the entire support.
The polynomial \(F_N\) itself satisfies the equations by Theorem 1
and is nonzero. This proves the assertion. \(\square\)

The support condition is essential. The shift equations alone,
on an unrestricted space of functions at a root of unity, do not
give this uniqueness conclusion. Also, (12) does not show
\(F_N(\mathbf1)\ne0\). A linear functional on a one-dimensional
space of coefficient arrays can annihilate its generator. The
original closing evaluation still requires its own estimate.

## 4. The associated algebraic equations

There is a direct classical algebraic system behind (9). Replace
the commuting shift symbols \(T_e\) by nonzero variables \(y_e\),
and take the level limit of their scalar coefficients. Thus
\(q^{\ell_c}\to1\) and \(q^d\to-1\). The result is
\[
 \prod_{e\ni v}y_e=-1,\qquad
 \prod_{e\in c_+}(y_e-y_e^{-1})
 =
 (-1)^{a^{\mathsf T}c}z^c y^{Hc}
 \prod_{e\in c_-}(y_e-y_e^{-1}).
 \tag{13}
\]
The factors \(i\) cancel because a cycle has equally many positive
and negative edges. These are Laurent polynomial equations over
\(\mathbb Q\). Their equations and degrees depend on the fixed
diagram, not on \(N\). On the regular open set
\(y_e-y_e^{-1}\ne0\), cycles multiply according to addition in
\(\ker_{\mathbb Z}C\). A lattice basis of cycles consequently
suffices for (13) on that open set. At the excluded divisors the
uncancelled equations must be retained.

To verify the stationary meaning rather than infer it formally,
choose local logarithms \(y_e=e^{\pi i x_e}\) with \(Cx=\mathbf1\).
On a regular simply connected chart choose an analytic primitive
\(\mathcal J'(x)=\log(2\sin\pi x)\), normalized to
\(\mathcal J=J\) on an interval in \((0,1)\), where
\(J(t)=\int_0^t\log(2\sin\pi u)\,du\). The local action is
\[
 \mathcal S(x;z)=
 -\sum_e\mathcal J(x_e)
 +\pi i\left(\frac12x^{\mathsf T}Hx+a^{\mathsf T}x\right)
 +\sum_e x_e\log z_e.
 \tag{14}
\]
Its real restriction at \(z_e=1\) has the same real part as the
concave angle expression in the complete-source note. Direct
differentiation gives
\[
 \exp(D_c\mathcal S)
 =
 (-1)^{a^{\mathsf T}c}z^cy^{Hc}
 \prod_e(2\sin\pi x_e)^{-c_e}.
 \tag{15}
\]
Thus (13) is precisely the exponentiated stationary equation
\(\exp(D_c\mathcal S)=1\). At a chosen solution, this means
\(D_c\mathcal S\in2\pi i\mathbb Z\), not automatically zero.
Those integers are additive on the cycle lattice.

For completeness they can be represented by an integer vector
\(r\in\mathbb Z^E\). Indeed \(\ker_{\mathbb Z}C\) is primitive:
its quotient in \(\mathbb Z^E\) is the subgroup
\(\operatorname{im}_{\mathbb Z}C\) of a free abelian group,
and is therefore free. Hence every integer functional on the
kernel extends to \(\mathbb Z^E\). Replacing (14) by
\(\mathcal S-2\pi i\,r^{\mathsf T}x\) makes all its tangent
derivatives vanish at that solution. This is the usual integer
Fourier ambiguity, retained explicitly here.

The equations \(\prod_{e\ni v}y_e=-1\) fix \(Cx\) only modulo
even integers. The actual source uses the lift \(Cx=\mathbf1\)
and the specified finite support. Neither that lift nor the
contribution of a stationary point is selected by (13) alone.

## 5. What this contributes to the geometric comparison

Equations (9) act on the exact original sum before a semiclassical
approximation. Equations (13) are a fixed algebraic object obtained
from them, and (14)--(15) check its relation to the angle action
and full quadratic phase. This makes the geometric comparison a
comparison of explicit equations rather than an assertion that
concavity must imply knot-group relations.

The joint-phase note supplies a further comparison: its independent
clock equations eliminate rationally, and the remaining regular
equations have the original physical crossing differential. The
earlier marked-braid notes already identify that physical
correspondence with meridian representations. This avoids treating
the classical representation comparison as a newly discovered
general theorem. It does not turn coefficient rigidity into a
nonzero contribution under the original evaluation. Theorems 1--2
prove no volume limit or finite-exception theorem.

The general use of hypergeometric state sums and difference equations
is established territory. Coverage references include
[Garoufalidis--Lê, *The colored Jones function is q-holonomic*](https://arxiv.org/abs/math/0309214)
and [Garoufalidis, *On the characteristic and deformation varieties
of a knot*](https://arxiv.org/abs/math/0306230).
No proof from those papers is used above. The derivation here checks
the precise finite root-of-unity support, its boundary cancellations,
and the actual prescribed phase; it makes no novelty claim for the
general difference-equation method.

## Direct source versions

| Source | SHA-256 |
| --- | --- |
| research_charged_source_angle_optimization.md, Sections 1--3 | 45b21fabb9cb65512bc3e576eb3d659b6fe14c3dcd90b4164bfdb12b8cedea64 |
| research_joint_clock_phase_equations.md, Sections 2--5 | 71393aa353909dfa2dd19b078b1d3fccdf8561520aa071b7537e4bbfc50bb867 |

Both written source implications were read in these versions. No
numerical results or executions are used in these proofs.
