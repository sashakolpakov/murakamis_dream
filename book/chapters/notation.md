# Notation and conventions

The guide uses the conventions below. Some older notes use the same letter for different objects, so their local definitions must be checked before formulas are combined. In particular, a tangle turn, a crossing matrix and a shift of the meridian variable are different operations.

## The invariant and the order of limits

Fix the knot diagram, its tangle expression and all integer twist weights first. Then let the quantum level \(N\) tend to infinity through all sufficiently large integers. A theorem with this order of limits does not give a threshold uniform over trees whose size grows with \(N\).

| Symbol | Meaning |
| --- | --- |
| \(N\) | Quantum level, an integer at least two. |
| \(q_N=e^{\pi i/N}\) | The root of unity used for the original symmetric quantum integers. |
| \(\zeta\) | A generic quantum parameter when differentiating before root specialization. |
| \([r]_\zeta=(\zeta^r-\zeta^{-r})/(\zeta-\zeta^{-1})\) | Symmetric quantum integer. |
| \(d=N-1\) | Top basis index in the \(N\)-dimensional physical color. |
| \(K_N(K)\) | The original reduced Kashaev invariant of \(K\), with unknot value one in the stated convention. |
| \(n_i\) | A fixed integer twist weight in the filled diagram. In a discussion of auxiliary colors the same letter may be used locally for a representation label; that local use is stated. |
| \(n_i=\epsilon_i-2p_i\) | Twist decomposition: \(\epsilon_i\in\{0,\pm1\}\) is a retained half twist and \(p_i\) is the signed integral filling parameter. |
| \(v_3,v_8\) | Volumes of a regular ideal tetrahedron and a regular ideal octahedron. |

The augmented exterior still contains the auxiliary crossing circles. Filling their cusps inserts the twists and produces the stated knot or link exterior. Its volume generally differs from the complete augmented volume. The main knot cusp is not filled.

## Finite sums, colors and derivatives

A **color** is a representation label carried by a strand or auxiliary circle. An internal **channel** is a representation label introduced by a change of basis. These are integer labels in a finite sum; allowing a related scaled variable to become complex requires a specified interpolation.

| Notation or term | Meaning and purpose |
| --- | --- |
| Source | The complete prescribed quantum expression: matrices, index sums, cups, caps, marked functional and scalar factors. “Full source” means the full quantum sum. |
| Core | A specified term in an exact color decomposition, usually the part carried by the complete-circle operator. |
| Alias | The complementary term in that same exact decomposition. Its smallness must be proved; the name does not make it negligible. |
| Packet | A local asymptotic formula with its action, nonzero prefactor and controlled remainder. |
| Normal | A derivative needed at a repeated spectral node or in a generic parameter. The differentiated variable is always part of the definition. |
| \(Z_{E,N}\) | The positive complete quantum sum of the specified expression \(E\), when that positive specialization is being discussed. It is not a name for every signed filled invariant. |
| \(W_N\) | A positive normalized local Racah scalar in the calculation with four external representation factors, not the entire knot invariant. |

At fixed \(N\), differentiating in \(\zeta=q_Ne^t\) is different from taking another term in an expansion as \(N\to\infty\). A zero root value can have a nonzero generic derivative. Similarly, values of a polynomial at repeated eigenvalues do not determine its first normal coefficients. Both distinctions are necessary for the original invariant.

## Tangles and geometric variables

A geometric gluing face is a quadrilateral with four ordered ideal vertices. Its vertex order determines the actual face identification. Some technical notes call this face a port; in algebraic formulas the same word can instead mean an external representation factor or a boundary index, which must be specified.

A tangle box has four ordered endpoints. Multiplication means the specified stack of two boxes. A physical quarter-turn rotates the box. The cylindrical closure joins lower endpoints to upper endpoints, whereas the cap closure joins the two upper endpoints together and the two lower endpoints together. Those closures can have different topology.

The guide writes \(R\) for a crossing operator and \(T\) for a tangle turn when discussing this grammar. Some older notes use \(R\) for the turn. In a quantum \(A\)-equation below, \(T\) instead denotes a difference operator; its action is explicitly given.

In a local theorem with four external representation factors, \(A,B,C,D\) may denote the four highest weights and \(E,G\) two intermediate highest weights. They are not the \(A\)-polynomial or the whole Conway expression. The half-shifted variable \(a_e=(j_e+1/2)/N\) determines a dihedral angle \(\alpha_e=\pi-2\pi a_e\). A cusp shape \(\tau_i\) is the complex ratio of two primitive translations on the marked Euclidean cusp torus.

For the auxiliary-color deformation, \(U_i,V_i\) denote specified logarithms of peripheral multipliers. They include branch choices and refer to the primitive curves of the actual diagram. A shape field or an algebraic elimination relation does not by itself identify those variables with the main knot's meridian and longitude.

## The main-meridian quantum \(A\)-period

The raw unrolled representation coordinate is \(x=q_N^\alpha\). The marked meridian coordinate is
\[
 M=-q_Nx.
\]
Thus the complete color \(\alpha=N-1\) has \(M=1\), while a quotient color \(\alpha=j-1\) has \(M=-q_N^j\). The reduced ADO family \(F_N(M)\) satisfies
\[
 F_N(1)=K_N(K),\qquad F_N(-q_N^j)=C_j(q_N),
\]
where \(C_j(q)\) is the ordinary reduced \(j\)-color period.

In an equation \(P(q,M,T)F=0\), the shift is \((TF)(M)=F(qM)\), so \(TM=qMT\). A classical longitude variable is usually called \(L\). It is distinct from a complete-circle operator \(L_N\) and from a recoupling coefficient \(L_{G,E}\).

The selected operator period also needs its fixed initial-color data. When a companion matrix has a pole at a root level, the prescribed value is the constant term of the entire product's Laurent expansion. One does not evaluate numerator and denominator separately at zero. The full ADO state carries its exact modified-dimension factor; at the complete marked point its value is \(i^{N+3}K_N/N\).

The [pointed operator theorem](../../notes/actual_conway_pointed_quantum_a_volume.md) proves the volume limit for this actual period on the covered strict long-twist knots. Identifying its selected classical main-meridian geometric factor remains a separate statement.
