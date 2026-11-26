# All-MAIN mark rerouting: exact local identities and the remaining adapter

31 October 2026. PRIVATE RESEARCH CHECKPOINT, NOT A THEOREM.
The existing top-cap transport theorem is unchanged. In particular this
note does not claim that replacing its protected pair by any MAIN edge
already gives a proved full-source identity. A finite test below is
diagnostic only. The potentially useful argument must change the actual
cut presentation, not insert the same rank-one matrix into an internal
head of the original presentation.

## 1. Proposed statement and precise source data

Let P(L)=product_e H_(f_e)(L_x,L_b,L_c,L_y) be the ORIGINAL homogeneous
polynomial of a connected complete-colored plat, with all full
Casimir polynomials and retained crossing matrices in their original
order. Its total degree is dR, d=N-1. For a MAIN edge separating faces
a,b, the proposed coefficient is

    Z_(a,b)=[product_(f!=a,b) L_f^d] P |_(L_a=L_b=0).

The reviewed top-cap theorem proves this equals the original marked
scalar when (a,b) is one of its original exposed top pairs. The question
is whether the equality holds for every MAIN edge of this same source.
No projected sector, individual face-flow, or absolute envelope would
be transported even if this full-polynomial statement were established.

The relevant source inputs are:

- notes/research_arbitrary_casimir_top_mark_transport.md, sections 2--4;
- notes/quantum_bridge_cap_source.md, formulas (1.3)--(1.4) and (2.1)--(2.4);
- notes/actual_original_marked_face_coefficient.md, sections 2--5;
- notes/actual_homogeneous_casimir_face_source.md, sections 3--4.

## 2. An unchanged-basis straight insertion is insufficient

The generic scalar-cut argument must not be identified with insertion
of a fresh g^(-1)e at an arbitrary internal physical head in the old
Morse presentation. A cut exposed on the outer boundary and an internal
head have different dual/pivotal boundary transport.

For example, take N=3, the literal width-two word [1,2,1], and full
numerators with spectra (2,-2,0). The original top-marked scalar is
648. In the original physical tensor calculation over F_1009, insert
either diag(g)/N or diag(g^(-1))/N at either internal head immediately
after the first box, leaving every other tensor unchanged. Both give
287, not 648. Whole-source weight conservation makes off-diagonal
entries of a putative rank-one insertion irrelevant in this test.
Thus this is also a test of those naive rank-one prescriptions.

This is not a counterexample to the proposed coefficient statement.
In the same example its six literal MAIN pairs are

    (0,1),(0,2),(0,4),(1,3),(2,3),(3,4),

and every corresponding two-zero coefficient of the unchanged P is
exactly 648. This distinction is the reason to seek the actual rerouted
cut adapter instead of inferring it from an abstract Schur argument.

For reproducibility the three local N=3 polynomials, with quartet
(x,b,c,y), are

    H_2=4b^2+bc-3b(x+y)+4c^2-3c(x+y)+9x^2+6xy+9y^2,
    H_(-2)=9bc+9b(x+y)+9c(x+y)+9x^2+18xy+9y^2,
    H_0=-2b^2+bc+3b(x+y)-2c^2+3c(x+y)+9x^2+12xy+9y^2.

The actual ordered quartets are (1,0,3,2),(3,2,4,0),(1,3,0,4).
The local formula follows directly from
V_3(sigma)=Omega^2+sigma Omega+(sigma^2-3)I and the actual triangular
Omega action, whose diagonal is (1,-2,1), monomer weights -3(x+y)
and allowed dimer weight -3xy. These exact finite computations are
not evidence of a general asymptotic estimate.

## 3. Exact four-turn identities at the complete color

There is a promising local simplification that is already algebraic.
Set q=exp(pi i/N), Q=q^2, x=q^d and

    g_i=x^(1-N) Q^(-i)=q^(-d^2-2i).

The four original balanced turn matrices are

    ev_L(a,b)=x^a/N delta_(a+b,d),
    coev_L(b,a)=N x^(-a) delta_(a+b,d),
    ev_R(b,a)=x^a g_b/N delta_(a+b,d),
    coev_R(a,b)=N x^(-a)g_b^(-1) delta_(a+b,d).

When each is written in its literal LEFT-TO-RIGHT ordered pair (i,j),
all four reduce exactly to

    cap(i,j)=N^(-1) q^(di) delta_(i+j,d),
    cup(i,j)=N q^(-d^2+di) delta_(i+j,d).             (1)

For the right cap, its ratio to the displayed expression is
q^(-2Ni)=1. For the right cup it is q^(2N(d-i))=1.
The left formulas are immediate. Thus (1) holds at both parities and
composite levels; it is not an off-root identity or a reset of a dual
frame.

There are also two explicitly different reduced cap prescriptions.
With e_(a,b)=1/N, the right cap uses D_R=g^(-1)e and the left cap
uses D_L=g e on its primal input. Their actual arrays are

    mark_R(i,j)=x^j/N^2,
    mark_L(i,j)=x^i g_(d-i)/N^2.

Both are unrestricted before contraction. On the complementary
support forced by a whole source with one exposed cap, i+j=d, the
second formula equals x^j/N^2 as well. Each pairs to one with its
corresponding original cup. This statement does not say either
prescription may be freshly inserted at an old internal head.

## 4. Candidate rerouted proof and its exact checkpoints

One can try to remove a point from face a of the spherical diagram,
make a the exterior, and pull a segment of the chosen MAIN edge into
an exposed cap through that now-unbounded face. All original coupon
disks should keep their ordered (x,b,c,y) frames; any new bends belong
to MAIN arcs. No crossing, framing twist, or independent scalar may
be introduced. The resulting presentation need only be Morse, not a
flat plat with all cups at the bottom and caps at the top.

For this proposed presentation the local identities in section 3
would make the remaining algebra identical to the original compiler:

1. Let M_f count original input/output middle corners and T_f the
   signed outside-minus-inside turn incidences of the new Morse arcs.
   The required general winding identity is M_f-T_f=2 for bounded
   faces and -2 for exterior a, with all local coupon frames fixed.
   It should follow by traversing each face boundary and retaining
   both kinds of physical bends. Merely citing the old flat-gap sweep
   is insufficient for this new presentation.

2. The ordinary whole source would then have character
   L_a^d product_(f!=a)L_f^(-d). The exposed cap's original SECOND
   head gives the marked ratio N^(-1)(L_b/L_a)^d. Both a,b exponents
   vanish and every other target stays d. The scalar from turns is
   N^(-1), since the closed Morse diagram has equally many cups and
   caps and only one cap is replaced. Their q^(d^2/2) constants cancel
   the cup constants exactly as in the reviewed flat presentation.

3. The actual unwrapped conservation lattice must still equal the
   primitive face-potential lattice of the unchanged planar graph.
   New degree-two turn vertices do not change its cycle lattice. The
   even coset is the same MAIN-odd/MATCHING-even cocycle, now gauged
   to t_a=0. The grid then has N^(R+1) states. With one factor N^(-1)
   per box and the marked N^(-1), it is a normalized average. Degree
   dR forces its unique alias to be exactly the displayed two-zero
   coefficient. Unsupported physical head totals must remain killed
   by the original full polynomial adapter, not reset modulo N.

4. Finally compare this actual rerouted reduced scalar with the old
   top-cap scalar. The regular generic-q lift from the existing mark
   theorem provides a candidate proof: moving the exterior across a
   MAIN edge exchanges the two pivotal closures of an intertwiner on
   the simple V_d (or its regular dual). That intertwiner is scalar,
   and both generic traces are [N]_q. Equality then specializes without
   dividing [N]_q at the root. Every move must retain the same coupon
   disks, their actual R^epsilon/Cartan scalars and framing.

5. The root pivot correction must be checked along those moves. Each
   actual right turn differs from the standard-K turn by (-1)^d.
   A left snake adds zero right turns and a right snake adds two;
   exchanging left/right trace closures uses one right turn on either
   side. This suggests that right-turn parity stays equal to the
   original k. Marking a right cap removes one such factor; marking a
   left cap adds one, giving the same parity k-1 in either case. A
   complete written move decomposition is still required before using
   this as the global normalization proof.

The local four-turn reductions (1) and the two marked cap arrays are
checked exactly. The five-step rerouted adapter, especially its fixed
coupon-frame isotopy and root pivot-parity bookkeeping, has NOT yet
received a complete proof-level review. Therefore the proposed
all-MAIN coefficient equality remains OPEN in this checkpoint.

No existing top-cap theorem, source-energy statement, guide or
publication file has been changed. The exact low-demand R_n inequality
also remains open; this marking question is a separate possible source
interface and is not a cancellation estimate.
