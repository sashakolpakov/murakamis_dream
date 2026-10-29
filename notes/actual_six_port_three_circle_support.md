# Actual six-port complete-circle support and the limits of tensor sampling

29 October 2026. Three disjoint complete-circle insertions have a genuine
source restriction: their observed joint channels lie in a tetrahedral
simplex, rather than an independent spectral cube. This necessary support
and a rank bound follow from the ORIGINAL saturated source, without an
assumed regular-cube eigenframe. Nonvanishing on all remaining channels
is a separate actual Clebsch/top-normal problem.

The positive all-value circle quotient is not a faithful norm for the
whole marked source. A faithful tensor Hermite reconstruction exists on
the scalar joint polynomial algebra, but its polynomial coefficient cost
does not bound the actual recoupling energy. These statements must be
kept distinct when proposing a six-port DCT sewing theorem.

## 1. The original source and its joint root blocks

Use d=N-1, M=floor(d/2), the original V_N, and the saturated source

    S_N=(Inv_K V_d(zeta)^tensor6 intersect V_d(O)^tensor6)/t,
    dim S_N=(N^3+N)/2,

where O is the analytic DVR at zeta=q_N and t=zeta-q_N. Equivalently
S_N is the literal divided-current kernel already proved in
[the six-port source theorem](actual_six_port_divided_power_source_kernel.md).
The three ACTUAL commuting pair Casimirs are A_1=Omega_12,
A_2=Omega_34,A_3=Omega_56. Generic pair nodes are

    c_a(zeta)=zeta^(2a+1)+zeta^(-2a-1), 0<=a<=d.

At the root, fold a to j=min(a,d-a), 0<=j<=M. The root cluster
J(j)={j,d-j} is double unless N is odd and j=M, in which case it
is the simple Steinberg node. Write E_J for the REGULAR joint cluster
idempotent and S_J=E_J S_N. Its dimension is the number of generic
triples

    (a,b,c) in J(j_1) x J(j_2) x J(j_3),
    |a-b|<=c<=a+b.                                     (1)

This is the actual flat-rank statement, not an ordinary semisimple
root quotient. The
[bounded-confluence theorem](actual_six_port_bounded_confluent_blocks.md)
keeps all normal coefficients and proves the regular cluster splitting.

On a double axis put N_i=A_i-c_(j_i); then N_i^2=0 on that cluster.
The full ordinary complete circle L_N has exactly

    L_N(A_i)=ell_i N_i, ell_i!=0, on a double cluster,
    L_N(A_i)=N I, on the odd simple Steinberg cluster.   (2)

For example ell_i=(-1)^d N/[2 sin^2((2j_i+1)pi/N)].
Thus the product of the three circles is a nonzero scalar times the
TOP product of the r double-axis nilpotents, where0<=r<=3.

## 2. A missing generic corner kills the top product EXACTLY

Suppose a triple alpha in the cluster cube violates(1). Its generic
joint eigenprojector p_alpha is ZERO on the generic invariant space.
On the regular cluster lattice it is a product of r factors

    (A_i-c_(partner(alpha_i)))/(c_(alpha_i)-c_(partner(alpha_i))).

Each denominator is t times a unit. Clear all those denominators.
The resulting regular numerator annihilates the cluster lattice over K,
hence over O, since that lattice is torsion free. Specializing at t=0
gives

    product_(double axes i) N_i=0 on S_J.               (3)

No condition-number, choice of generic eigenbasis, or maximal minor
enters(3). It is a cleared ACTUAL projector identity. In particular,
the result does not infer a Jordan module just from its eigencharacters.

All corners of the folded cube satisfy(1) if and only if

    j_1+j_2+j_3>=d.                                    (4)

Indeed, if their sum sigma is<d, the allowed corner
(d-j_i,j_j,j_k) violates the triangle inequality. If sigma>=d,
any chosen coordinate is at most d-j_i, while the other two have
sum at least sigma-j_i>=d-j_i. Every triangle inequality follows.
The same proof includes a simple Steinberg axis, for which the two
possible labels happen to coincide.

Consequently L_N(A_1)L_N(A_2)L_N(A_3) is ZERO on EVERY source block
outside(4). This is a necessary all-level source support theorem.

## 3. On a surviving block its rank is at most one

For a block satisfying(4), dim S_J=2^r. The commuting nilpotents
give it a module over

    R_r=C[epsilon_1,...,epsilon_r]/(epsilon_1^2,...,epsilon_r^2).

Every nonzero ideal of R_r contains its one-dimensional socle
C epsilon_1...epsilon_r. To prove this, start with a nonzero ideal
element and multiply by a maximal nonvanishing product of epsilon_i.
The result is killed by every epsilon_i; expansion in the monomial
basis shows it is a nonzero multiple of the top monomial.

If the top product acts nontrivially on v in S_J, its annihilator
cannot contain a nonzero ideal, hence Ann(v)=0. Then R_r v has
dimension2^r and is all of S_J. The module is the regular cube module,
and its top product has rank1. Otherwise that top product has rank0.
For r=0 the block has dimension1 and the product in(2) is already
nonzero. Thus the restricted three-circle rank is always0 or1 per
surviving cluster; regular-cube structure is a CONSEQUENCE of a
nonzero top product, not an assumption used to prove it.

Put h_i=M-j_i and K=3M-d. Condition(4) is exactly

    h_1,h_2,h_3,e>=0, h_1+h_2+h_3+e=K.                (5)

Since K<=M, no further h_i upper bound is needed. If K<0 the observed
source is zero; otherwise

    rank[L_N(A_1)L_N(A_2)L_N(A_3)|S_N]
                                 <=binom(K+3,3).       (6)

It is NOT yet proved here that every allowed top product is nonzero.
Generic rank2^r does not force that: a diagonal O-lattice with the
same generic corner eigenvalues specializes to zero nilpotents,
whereas the cube coordinate order specializes to the regular module.
The actual physical source lattice distinguishes these examples.

There is one constructive nonzero family at every ODD N. Fix two axes
at the simple Steinberg j=M. Their generic highest weight2M=d and all
ladder factorials have index<N, so their pair embeddings are regular
O-direct summands isomorphic to the original V_N. The projected source
is therefore the FOUR-logical-head invariant source. That already
proved complete source is the regular N-dimensional Casimir algebra
H_N; its remaining pair Casimir has its full double Jordan blocks.
The third circle consequently has rank1 at every (M,M,j), and likewise
for the two other permutations. These give3M+1 nonzero channels,
including their shared simple corner. No norm bound on the embedding
or its inverse is being inferred. Interior allowed channels and the
even-level nonvanishing still require their actual top coefficient.

## 4. Positivity, marking, and what tensor DCT does not imply

Let P_i be the physical leg exchange in pair i and C_i=P_i L_N(A_i).
The exact reflection theorem makes C_1 tensor C_2 tensor C_3 positive
semidefinite. Its radical on S_N is the kernel of the three-circle
product, since the product of the exchanges is invertible. Sections2--3
therefore describe a genuine observed quotient. It is not faithful on
S_N, and its nodes have simplex support(5), not tensor-product support.

The original marked co-source cannot silently be replaced by three
ordinary cap functionals. The companion
[actual marked-metric calculation](actual_three_belt_saturated_source_and_marked_metric.md)
retains the ordinary C/marked H distinction and the full marked row.
In particular the all-C form cannot give a finite Riesz dual for that
whole original marked functional. The marked H form changes the
source/leg wiring and must be analyzed on its own; its extra channels
are not licensed by the ordinary simplex theorem above.

There is now a constructive correctly marked alternative, proved in
[the actual multiport Chebyshev packet](actual_marked_multiport_chebyshev_source_packet.md).
Extract the physical degree-d component of each final pair AFTER using
the total-degree constraint. Its full CD transform uses f_a on the
ordinary variables and f_a# on the marked variable. For six ports it
gives the exact original corner

    K_raw=x^d N^(-4) F_N(c_0,c_0,c_0)

and positive energy N^3 sum_grid m_1m_2m_3|F_N|^2. Folding only after
this actual CD identity gives degree<=M in every variable, with exact
tensor DCT/Parseval and squared marked dual norm1/(8N^5) in its
coefficient norm, equivalently1/(8N^11) against that energy. It avoids
the ordinary three-C radical by keeping the marked conjugation and
its current. The transform's coherent energy is not yet bounded by
the geometric partition, and the observation kernel is not assumed
stable under arbitrary interior split-pair braids. Thus this is a
source-compatible positive correction, not a contradiction of(3)--(6).

A tensor version of the exact one-variable Hermite DFT is nevertheless
available on the FULL scalar algebra H_N^tensor3. Set

    ||F||_(H,3)=sum_(nu in {0,1}^3) N^(-2|nu|)
                   max_jointnodes |partial^nu F|,

where a differentiated axis ranges only over its double nodes and
an undifferentiated axis includes the odd simple node. This is faithful
and submultiplicative. Applying the explicit one-variable reconstruction
in [the full circle algebra](general_augmented_graph_source_extension.md),
section4, in each variable gives, for coefficients beta in the basis
L_a tensor L_b tensor L_c,

    ||F||_(H,3)<=(3/2)^3 N^(9/2)||beta||_2,
    ||beta||_2<=6^3 N^(9/2)||F||_(H,3).                 (7)

All eight mixed jets are retained; no confluent Vandermonde inverse
or hidden Casimir normal is discarded. This is a coefficient theorem
on the full commutative algebra. Identifying its quotient with an
actual six-port source frame, or bounding a recoupling map in it,
still needs the actual frame/measure and marked dual norm. In particular
it is not ordinary DCT with independent positive product weights on(5).

There is already an exact actual norm warning in one variable. At
N=4r the complete Newton multiplication kernel has

    |(T_1)_(2r,r)|=s_(2r)/s_r^2,
    lim_(r->infty) N^(-1)log|(T_1)_(2r,r)|=v_8/(4pi)>0,

whereas the faithful Hermite norm of the SAME full original crossing
obeys ||R||_H<=9/8. Thus a polynomial Hermite/Fourier coefficient
reconstruction does not imply a polynomial bound for its actual
Newton multiplication energy. The four-head packet embeds regularly
in the six-head source by tensoring its original cup. This warns
against the proposed automatic metric identification; it does not
rule out a different coherent marked geometric Gram.

## 5. Coverage only

Van der Veen's [primary main theorem](https://arxiv.org/html/0805.0094#S1.T2)
already treats sufficiently augmented knotted trivalent graphs from
each fixed construction sequence. Its quantum statement uses odd N;
the theorem explicitly gives zero at even N and concludes the SO(3)
volume conjecture. Its singly augmented outside is described by regular
ideal octahedra; additional parallel augmentation circles can contribute
Seifert JSJ pieces. These are important coverage and normalization
qualifications, not an all-N original-source six-port estimate supplied
by that theorem. Only the introduction/main statements were inspected;
no proof technique or state-sum replacement is used here.

The next useful actual calculation is the coherent trivalent top-normal
coefficient and its positive/marked measure on(5), followed by its
recoupling energy. Neither(7) nor the generic triangle count proves
that analytic comparison. The support restriction(3)--(6) itself is
an exact source theorem and is available before that estimate.

Audit: [exact folded incidence, simplex count and truncated-cube rank lemma](../experiments/audit_actual_six_port_three_circle_support.py).
Fresh checks pass all folded channels at N=2,...,40 and the four
r=0,1,2,3 regular-cube algebra models. These integer/model checks
supplement the cleared-projector proof; they do not extrapolate
actual interior top-normal nonvanishing from finite examples.
