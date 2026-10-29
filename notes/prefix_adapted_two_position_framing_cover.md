# Actual prefix clocks give a quadratic framing cover with a twisted density

Research theorem, 27 October 2026. The physical Gauss meridian on
an internal edge is not its developed Wirtinger meridian. Retaining
the actual prefix adapter shows that ANY two physical position
clocks have degree at most two on the framing torsor; braid length
does not increase that degree. The density is generally NOT odd
under the quadratic deck transformation. Its exact field trace is
computed below, including a nonzero actual figure-eight example.

The local wave momentum still has a reciprocal deck law at the
complete point. Together with an ACTUAL prefix clock insertion,
the nearest two-cut bands realize a nonzero local orientation
observable. None of these calculations selects the global framing
cycle or identifies its field trace with the original quantum source.

## 1. Actual Gauss reconstruction retains both prefix products

At any level of an arbitrary mixed braid word, write the developed
meridians as H_1,...,H_b in the convention of
[the actual holonomy proof](marked_braid_holonomy.md). The physical
meridians are mu_i=-H_i; their trace is M+M^(-1). Set

    P_j=H_j...H_1,
    V=mu_(j-1)...mu_1=(-1)^(j-1)P_(j-1),
    U=mu_j...mu_1=(-1)^j P_j.                       (1.1)

For a fixed representation these are fixed determinant-one matrices;
their entries lie in its marked algebraic representation field.
Changing the framing by F conjugates EVERY prefix simultaneously.
At a new braid level the Hurwitz words defining U,V change, but
the following formulas are unchanged.

For a determinant-one matrix P write

    B_-(P)=[[1,0],[-P_21,P_11]],
    B_+(P)=[[P_11,P_12],[0,1]].

The exact inverse of the developed holonomy map gives

    b_(+,j)=B_+(P_j)B_+(P_(j-1))^(-1),
    b_(-,j)=B_-(P_j)B_-(P_(j-1))^(-1),
    K_j=(P_j)_11/(P_(j-1))_11.                    (1.2)

In particular, if a_l=(P_l)_11, b_l=(P_l)_12,
c_l=(P_l)_21, then the local physical entries are

    e_j=b_j-K_j b_(j-1),
    K_j f_j=c_j-K_j c_(j-1).                      (1.3)

These identities follow by multiplying the displayed triangular
matrices. They are identities of the actual classical crossing
graph; no developed matrix is substituted for G_j.

Classically x=-M and K_j=x/A_j. Consequently the SIGNED physical
inverse position is

    k=-K_j=M/A_j=(F^(-1)UF)_11/(F^(-1)VF)_11.      (1.4)

At completeness M=1, write B=A_j=1/k. At a literal finite
quantum level x=-M/q; that extra q factor is retained below.

## 2. Degree at most two is independent of every prefix word length

At the complete point choose the reference cut meridian
J=[[1,1],[0,1]] and the actual cut-framing chart

    F(r,s)=[[r,1-r],[s,-s]], s!=0,
    tau=r/s, A=1/(1+s).

The selected inverse flag is 1. Its rank-one projector is

    P_fr=F E_11 F^(-1)
        =[[r,r(1-r)/s],[s,1-r]].

For ANY fixed matrix W=[[a,b],[c,d]], define

    ell_W=Tr(W P_fr)
         =d+(a-d)r+bs+c r(1-r)/s
         =d+c tau+s[b+(a-d)tau-c tau^2].            (2.1)

Thus the ACTUAL second position is the ratio ell_U/ell_V, not
ell_(mu_j). Put C=U-kV. Its fiber equation is

    ell_C=0.                                     (2.2)

This is a quadratic in tau, with coefficients depending on s,k.
Therefore a generically finite two-position chart has degree one
or two, NEVER a degree growing with the braid or prefix length.
Common factors or a linear fiber can reduce the degree. Etaleness
means the actual local derivative below is nonzero; it does not
force the degree to be exactly two.

There is a coordinate-free version at varying M. The projector
coordinates r,s,t obey r(1-r)=st, and every ell_W is affine linear
in them. Fixing the first physical clock is one affine hyperplane
condition; fixing ell_U/ell_V is a second. Their intersection with
this quadric has length at most two on a generically finite chart.
All M-dependent eigenvalues and flags remain marked. No positivity
or geometric action estimate is needed for this degree statement.

Let h_C=a_C-d_C, t_C=Tr C, c_C=C_21, and set

    D=partial_tau ell_C=c_C+s h_C-2s c_C tau.

On the fiber,

    D^2=Delta=c_C^2+2c_C s t_C
                              +s^2(t_C^2-4 det C).              (2.3)

Since UV^(-1)=mu_j has trace M+M^(-1),

    det(U-kV)=(k-M)(k-M^(-1)).                    (2.4)

At M=1 this is (k-1)^2. Formula (2.3) follows by taking the
discriminant of (2.2), not by treating C as a unipotent matrix.
When c_C!=0, the deck map is

    tau -> (c_C+s h_C)/(s c_C)-tau, D -> -D.       (2.5)

## 3. The actual density has an essential prefix factor

The complete framing density is Omega_cut=d tau wedge dlog A.
Differentiate ell_U-k ell_V=0, fixing the representation. At
fixed s this gives

    dk=(D/ell_V)d tau.

Consequently, on the actual regular etale chart,

    Omega_cut=ell_V/(B D) dlog A wedge dlog B.       (3.1)

The numerator ell_V is part of the physical prefix adapter.
It generally differs on the two sheets. Thus D changing sign
does NOT imply that Omega_cut is anti-invariant.

Write c_W=W_21 and h_W=W_11-W_22, and put

    W_0=c_V h_U-h_V c_U.

For a genuine quadratic fiber, direct root summation gives

    Tr_(two sheets)(ell_V/D)=W_0/(c_U-kc_V)^2.

Indeed ell_V has coefficients -s c_V, c_V+s h_V,
d_V+s b_V. Reduce it modulo the quadratic ell_C; its remaining
linear coefficient is s(h_V c_C-c_V h_C)/c_C. Divide the
difference of its two values by the corresponding opposite
derivatives D; the result is exactly the displayed expression.
Multiplying (3.1) gives

    Tr Omega_cut
      = W_0 B/(B c_U-c_V)^2 dlog A wedge dlog B.    (3.2)

This is GENERALLY NONZERO. The earlier odd-density special case
V=I has W_0=0, as do some other special prefixes.

Nonzero field trace does not prove a nonzero period. On this
rational chart (3.2) is exact. If c_U!=0, its primitive is

    beta=(W_0/c_U)/(B c_U-c_V) dlog A,
    d beta=Tr Omega_cut.                           (3.3)

If c_U=0,c_V!=0, take beta=-W_0 B/c_V^2 dlog A instead.
The double pole has no ordinary logarithmic residue. An actual
relative endpoint/cycle can still see it; it cannot be assigned
or erased by replacing the source with an unmarked field trace.

These density coefficients are intrinsic MARKED character data,
rather than adjustable framing parameters. For J=[[1,1],[0,1]],
direct multiplication gives

    c_W=Tr(JW)-Tr(W),
    W_0=Tr[J(VU-UV)]=-Tr([J,U]V).                 (3.4)

Conjugation by the residual centralizer Z_t=[[1,t],[0,1]] of J
fixes c_W and sends h_W to h_W-2t c_W. It therefore fixes W_0,
lambda=c_V/c_U and gamma=W_0/c_U^2. Common conjugation of the
marked triple also leaves the trace expressions unchanged.
These are rational functions of its marked character. On a
geometric representation cover finite over the marked peripheral
curve they are algebraic over its A-curve field; they need not
be rational functions of M,L alone.

The [whole cyclic density calculation](cyclic_framing_density_source.md)
keeps the resulting exact source character 1-lambda^N. Its
finite root averaging is a separate algebraic functional, not
an automatic interchange with the selected Gaussian/source map.

## 4. The actual local wave momentum still detects the deck sign

Let primes mean conjugation by the SAME F. On a fixed k fiber,

    C'=F^(-1)(U-kV)F=[[0,beta],[gamma,t_C]].

Equations (1.2)--(1.3), including their signed prefixes, give

    beta=(-1)^j(k-M^(-1))p_j,
    gamma=(-1)^(j+1)(k-M)/p_j,                    (4.1)

where p_j is the ACTUAL balanced/factorial local wave momentum.
Equivalently e_j=(k-M^(-1))p_j and
f_j=(k-M)/(k p_j). The product in (4.1) is compatible with
det C=(k-M)(k-M^(-1)); no peripheral factor is discarded.

At M=1 the cut matrix in the current physical frame is
[[1+s,-s],[s,1-s]]. The invariant Tr(J C), together with fixed
s,k,t_C, fixes beta-gamma. Moreover direct differentiation of
F gives

    F^(-1)partial_tau F=s[[1,-1],[1,-1]],
    D=s(beta+gamma).                              (4.2)

Thus the deck map sends (beta,gamma) to (-gamma,-beta), and

    p_j -> p_j^(-1),
    D=(-1)^j s(k-1)(p_j-p_j^(-1)).                (4.3)

This proof uses the ACTUAL physical Gauss reconstruction. It
does not assume that G_j equals a developed H_j. All prefix
effects have already entered U,V and (4.1).

For reference a genuine regular quadratic generic-meridian fiber
has the corresponding twisted reciprocity. With the actual first cut inverse clock
k_0 and p_cut=1, its physical meridian is

    [[k_0,M^(-1)-k_0],[k_0-M,M+M^(-1)-k_0]].

The invariant pairing with C fixes a linear combination
of p_j and p_j^(-1), so the other sheet is

    p_j -> [(k_0-M^(-1))/(k_0-M)]
                   [(k-M)/(k-M^(-1))] p_j^(-1).   (4.4)

This is stated on the regular chart where the displayed factors
are nonzero. The complete specialization of (4.4) is (4.3).
No complete-point sign formula is extended across its singular
Gauss boundary by separately evaluating a zero and denominator.

## 5. A prefix-adapted odd observable comes from actual clocks and bands

The [physical two-cut theorem](actual_two_cut_framing_port_reconstruction.md)
proves for the nearest actual exchange bands, with their original
input/output and factorial marks,

    R_(+1,-1),0=p_j^(-1),
    R_(-1,+1),0=p_j.

Put z=s(k-1). By (4.3),

    R_(+1,-1),0-R_(-1,+1),0=(-1)^(j+1)D/z.        (5.1)

Its product with (3.1) still contains ell_V, so it need not be
deck-even. There is an ACTUAL finite source/current insertion
that supplies the missing inverse prefix. Telescoping (1.2) gives

    ell_V=M^(j-1) product_(i<j) A_i^(-1).

At a literal finite level K_i=x Q^(-J_i), x=-M/q. Therefore the
inverse signed quantum prefix is exactly

    [(-1)^(j-1) product_(i<j)K_i]^(-1)
          =(q/M)^(j-1) product_(i<j)Q^(J_i).       (5.2)

It is a product of ORIGINAL diagonal edge clocks, with its full
q/M meridian factor. It is not an invented density or a scalar
chosen after source evaluation. Its principal symbol is ell_V^(-1).
The ordered crossing/cap currents of this insertion remain those
of the actual word; it is not declared central through them.

At M=1 the prefix-adapted principal band observable

    ell_V^(-1)(R_(+1,-1),0-R_(-1,+1),0)
                               =(-1)^(j+1)D/(z ell_V)

is odd under the TWISTED density law, in the precise sense that
its product with the density has the nonzero DECK-EVEN value

    (-1)^(j+1)/(B z) dlog A wedge dlog B.           (5.3)

It realizes the normalized orientation section D/ell_V by an
actual bounded clock/band insertion. The prefix length j-1 is
fixed by the diagram, not by N. Formula (5.2) also specifies its
whole meridian/lift adapter before any quantum jets are taken.

The uninserted quantum period has not been replaced by (5.3).
Whether its original co-source/relative cycle provides this
particular inserted section remains a separate actual-current
comparison. In particular a nonzero local even density is not
already a nonzero globally selected framing period.

## 6. A genuine figure-eight prefix has nonzero field trace

Consider the ACTUAL three-strand braid (1,-2,1,-2). In its
Hurwitz convention put

    A=[[1,1],[0,1]], B=[[1,0],[-u,1]],
    u^2+u+1=0,
    C=B A^(-1) B A B^(-1).

The positive Hurwitz move is (X,Y)->(X^(-1)YX,X), and its
inverse is (X,Y)->(Y,YXY^(-1)). Direct multiplication fixes
the triple (A,B,C) under the displayed braid: its equations are
C A C^(-1)=B and C=B A^(-1)B A B^(-1). Every matrix has trace
two and determinant one. A and B have distinct fixed flags,
so this parabolic representation is irreducible. This is an
explicit actual knot-representation example, rather than an
arbitrary unrelated pair of matrices.

For the physical third strand the SIGNED prefixes are

    V=BA=[[1,1],[-u,1-u]],
    U=CV=[[u+1,2u+1],[-u(u+2),1-3u-2u^2]].

They give

    W_0=-u^2(u+2)=2u+1 != 0.                      (6.1)

For instance at s=1,k=2, c_C=1+u and the quadratic discriminant
is -3(u+4), both nonzero. Formula (3.2) has coefficient
2-2u, which is nonzero. Thus the blanket anti-invariance assertion
fails on an irreducible parabolic representation of the actual
figure-eight braid. The degree-two cover, the corrected momentum
deck law, and the ACTUAL prefix normalization (5.2) remain valid.

Exact audits: [script](../experiments/audit_prefix_adapted_two_position.py)
and [results](../experiments/prefix_adapted_two_position_results.json).
The reconstruction, trace, momentum signs and whole clock adapter
have a separate [independent proof audit](two_cut_port_band_current_audit.md).
