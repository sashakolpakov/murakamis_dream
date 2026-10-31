# Primary-source coverage of the root-normal planar-network period

29 October 2026. This is a definitions and theorem-scope comparison only.
It neither imports nor endorses the papers' proofs. No identification of our
period with a named invariant is asserted from terminology or matching growth.

The source object being compared is the exact period in
[the original NC Morse-graph reduction](actual_nc_morse_graph_first_normal_source_reduction.md):

\[
 q_*=e^{\pi i/N},\quad \zeta(t)=q_*e^t,\qquad
 Z_\Gamma=\frac{C_\Gamma}{\nu_N}
       \left.(S_\Gamma\Xi_\Gamma)'\right|_{t=0}.
\]

Here \(\Xi_\Gamma\) uses the specified ordinary canonical ordered 3j tensors;
\(S_\Gamma\) is the explicit product of source coefficients. The labels satisfy
\(0\le j_e\le(N-1)/2\). When every vertex is supported,
\(\sum_{e\ni v}j_e\ge N-1\), the source factors are nonzero at the root and
\(\Xi_\Gamma(0)=0\). Thus this case retains a **fixed first normal**, even
when that normal itself vanishes. The distinct marked-white boundary case
is retained in the cited source theorem.

## Closest root-normal definition

**Costantino–Guéritaud–van der Veen, _On the volume conjecture for polyhedra_,
arXiv:1403.2347, §1.2.2 (Evaluation), Conjecture 1.3 and Theorem 1.4.**
Their \(\operatorname{ev}_N(f)\) extracts the first **nonzero** Laurent
coefficient about \(A_*=e^{\pi i/(2N)}\); for their unitary spin network,
whose square is meromorphic, they extend this by a square root, up to sign.
The polyhedral volume statement uses \((\pi/N)\log|\operatorname{ev}_N
\langle\Gamma,c_N\rangle^U|\). Theorem 1.4 establishes the stated limit for
the tetrahedron-derived local-move family shown there. The paper explicitly
notes that this family excludes the cube; its general-graph statement remains
a conjecture, with an additional conditional result. [Primary paper](https://arxiv.org/pdf/1403.2347).

This is the closest prescription found, but it does not fix the order to one.
For a regular scalar \(f\) with a simple zero, our coordinate convention gives
\(\partial_t f=(A_*/2)\operatorname{ev}_N(f)\), since \(\zeta=A^2\).
At a higher-order zero our first normal is zero and their extracted
coefficient is not. The canonical/unitary vertex factors, their root orders,
and \(C_\Gamma S_\Gamma/\nu_N\) have not been equated.

The earlier **Costantino, _6j-symbols, hyperbolic structures and the Volume
Conjecture_**, Geometry & Topology 11 (2007), 1831–1854, likewise explicitly
studies the lowest Laurent term of quantum 6j-symbols, and gives results for
fundamental shadow links in connected sums of \(S^2\times S^1\). This is
additional coverage of the leading-term prescription, not an identification
of every fixed-first-normal planar network. [Primary paper](https://arxiv.org/abs/math/0611399).

## Named neighboring invariants

| Primary definition | Exact relevant domain and comparison |
|---|---|
| **Yokota invariant**, in Belletti, _An upper bound conjecture for the Yokota invariant_, Definitions 2.2, 2.5, 2.7; Theorem 4.9 | Odd \(r\), \(q=e^{2\pi i/r}\), even integer colors at most \(r-2\), with triangle sum at most \(2r-4\). For a trivalent graph, \(Y_r=|\langle\Gamma,\mathrm{col}\rangle^U|^2\), with unitary theta evaluation 1; higher valence uses a weighted desingularization sum. No fixed root derivative occurs in this definition. Its upper-bound theorem covers graphs generated from the tetrahedron by the two specified vertex/face moves; the geometric supremum is the volume of the right-angled rectification. Under the naive identification \(r=N\), integer colors \(2j_e\) in our supported sector have sum at least \(2N-2\), outside that admissibility cutoff. Root, color and normalization changes therefore require an explicit comparison. [Primary paper](https://arxiv.org/pdf/2002.01904). |
| **Renormalized Reshetikhin–Turaev invariant**, Geer–Patureau-Mirand–Turaev, _Modified quantum dimensions and re-normalized link invariants_, §3, Theorem 3 | For closed colored ribbon graphs admitting an allowed simple cut color \(V\), the definition is \(F'(L)=d_J(V)\langle T_V\rangle\), where \(d_J(V)=d_0S'(V,J)/S'(J,V)\) and \(d_0\ne0\) is a chosen scale. This is a cut/modified-dimension prescription, including root-of-unity examples. The theorem is not a definition by a fixed first derivative of an arbitrary ordinary integral spin network. Equality would need the cut category, vertex lifts and scale matched. [Primary paper](https://arxiv.org/pdf/0711.4229). |
| **Logarithmic knot invariant**, Jun Murakami, _From colored Jones invariants to logarithmic invariants_, introductory Theorem 1 | At \(\xi=e^{\pi i/N}\), the named invariant obeys \(\gamma_s^{(N)}=\frac{\xi}{2N}\partial_q[(q-q^{-1})(V_s+V_{2N-s})]_{q=\xi}\), \(1\le s\le N\). The paper identifies \(\gamma_N^{(N)}\) with its Kashaev normalization. This is a genuine root-derivative formula, but for knots and this prescribed combination of colored Jones polynomials, rather than our arbitrary canonical 3j network with its source factors. [Primary paper](https://arxiv.org/pdf/1406.1287). |
| **Colored-Alexander/SL(2,C) graph invariant**, Costantino–Murakami, _On SL(2,C) quantum 6j-symbols and their relation to hyperbolic volume_ | The graph invariant uses nonintegral quantum-group representations and extends a colored Alexander invariant. Its tetrahedral volume results do not, by definition alone, cover the ordinary integral-label first-normal network above. [Primary paper](https://arxiv.org/abs/1005.4277). |

The word “renormalized” is also used for a separate operation in
Costantino, _Integrality of Kauffman brackets of trivalent graphs_: multiplying
the generic bracket by explicit quantum-factorial factors to obtain an
integral Laurent polynomial. That is not itself a root-normal prescription.
[Primary journal definition](https://doi.org/10.4171/QT/49).

## Augmented graphs and right-angled link complements

**Van der Veen, _The volume conjecture for augmented knotted trivalent
graphs_, Definition 2, Definition 7 and Theorem 2.** For a fixed KTG move
sequence \(\mathcal S\), the theorem supplies a threshold \(n(\mathcal S)\):
each unzip must receive at least that many augmentation rings. At
\(A=e^{\pi i/(2N)}\), the normalized invariant is
\(\phi_N^{\theta}N^r\mathrm{sixj}_N^{t+1}\) for odd \(N\), and zero for
even \(N\), where \(t\) counts triangle moves, \(r\) rings, and
\(\mathrm{sixj}_N=\sum_{k=0}^{(N-1)/2}\left[\begin{matrix}(N-1)/2\\ k\end{matrix}\right]^4\).
Its outside has volume \((2t+2)v_8\). Normalization divides by the bracket
of the \(s\)-fold unlink for **split components**, not all link components.
Thus this is substantial augmented-graph/odd-\(N\) coverage, with an exact
central quartic factor. It does not state coverage of every singly augmented
NC Morse graph at both parities. A literal graph mapping and the prescribed
normalization are still needed. [Primary paper](https://arxiv.org/pdf/0805.0094).

**Ibarra–McQuire–Purcell, _Augmented links, shadow links, and the TV volume
conjecture: a geometric perspective_**, Theorems 2.12 and 4.15. The paper
identifies octahedral fully augmented link complements with fundamental
shadow-link complements, and states the Turaev–Viro volume limit for
octahedral fully augmented links with no half-twists, at
\(q=e^{2\pi i/r}\), odd \(r\). For \(c\) crossing circles the volume is
\(2(c-1)v_8\). This covers a related geometric class and a different quantum
invariant; it does not define our derivative period.
[Primary journal paper](https://nyjm.albany.edu/j/2026/32-1p.pdf).

## Coverage conclusion

Among the checked definitions, **leading Laurent evaluation**, **renormalized
RT**, **logarithmic knot invariant**, and **Yokota invariant** are different
prescriptions. None of the checked statements directly names or covers the
entire weighted fixed-first-normal period above for every original NC Morse
graph. This is not a claim that no such identification exists elsewhere.

Any claimed coverage must specify the variable and normal coordinate, root
order, canonical versus unitary vertex factors, color lattice, original
single marked cut and framing factors, graph construction, and parity.
No proof technique from these sources is used in this comparison.
