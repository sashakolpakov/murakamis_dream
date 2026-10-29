# A strict Fock-to-cyclic-normal Mellin map and its logarithmic obstruction

Research construction, 27 October 2026. This gives an explicit linear
comparison from the actual completed Fock source to the whole cyclic
normal source, including its Weyl operators, cut, pivot adapter and
relative endpoint carry. The target must retain a marked logarithmic
torsor. A global algebraic comparison with the same nonzero vacuum
and normal derivative is impossible on every finite cover.

The comparison below is between specified source/normal complexes.
It is not an algebra map of fixed-N matrix algebras and does not
identify their full quantum-group actions. It also does not fix the
physical 2pi*i adapter required for a geometric Fourier integral.

## 1. The two actual source modules and the explicit map

Fix a primitive N-th root Q in characteristic zero. In
[the common-Verma source](common_verma_two_wall_source.md), write
the completed Fock module as

    Fhat=H[[t]], h_j t^r/r!=v_(rN+j),
    B=partial_t, T=t, [B,T]=I, 0<=j<N.

Here H is the original balanced finite head, with source psi=1
and co-source phi=(1/N)sum_j. Its block vacuum projection is pi_0.

Retain the whole cyclic normal algebra and physical derivative:

    Chat=k[[U-1]][A]/(A^N-U),
    D_phys=A partial_A+N U partial_U,
    nabla=D_phys/N.

Mark alpha(U)^N=U, alpha(1)=1. Put u=Log U, u(1)=0, and

    epsilon_j=(1/N)sum_(l=0)^(N-1)Q^(-jl)(A/alpha)^l.

These are mutually orthogonal idempotents summing to one. They
evaluate to delta_(j,a) on A=alpha Q^a, and nabla epsilon_j=0.
The literal topological linear isomorphism is

    M(v_(rN+j))=epsilon_j u^r/r!.                (1.1)

It is invertible because the epsilon_j form a basis over k[[U-1]]
and u is a formal parameter with first coefficient U-1. Directly,

    M B=nabla M, M T=(Log U)M,
    M theta_s(h_j)=epsilon_j U^s.                (1.2)

Thus all integer resonant sectors U^k are present as the images
of coherent kernels theta_k. They are functions of the whole
normal U, rather than being set to one before transport.

This is an exact normal polarization comparison. It does not say
that the actual clock q-normal, block-number operator T B, and
nabla are the same operator. In particular M(T B)=u nabla M;
other current directions must be transported with their own marked
operator adapters, not inferred from (1.2).

## 2. The original cut and its normal pivot line are preserved

Let tau=Tr_(Chat/k[[U-1]])/N. The canonical A-power basis gives
tau(f)=f_0(U), and tau(epsilon_j)=1/N. Hence

    [tau M(f)]_(U=1)=phi pi_0(f),
    M(psi)=1,
    tau nabla=U partial_U tau.                  (2.1)

There are two different source projectors. The coefficientwise
extension e_H tensor I is carried to f |->tau(f)1, retaining every
normal coefficient. The actual finite-rank ambient coupon
Gamma=i e_H pi_0 is instead carried to

    f |-> [tau(f)]_(U=1) 1.

They agree on the vacuum but not on its first normal. In particular
the first projector commutes with nabla, whereas

    [nabla,Gamma_U]f=-[tau(nabla f)]_(U=1)1.     (2.2)

This is the additional finite normal cut row. It cannot be discarded
by identifying the whole-normal and finite-vacuum projectors.
These are strict linear cut comparisons, without identifying
matrix composition with scalar coefficient multiplication.

The root pivot also has two distinct whole-normal lifts. With
K_U=xA^(-1), define

    g_red=x^(1-N)A^(-1), g_lit=K_U^(1-N)=U g_red,
    D_red=g_red^(-1)e, D_lit=U^(-1)D_red.        (2.3)

The reduced representative agrees with the original pivot on U=1.
Only g_lit is its literal clock power off that fiber. In the
horizontal epsilon frame the exact adapters are

    g_red=alpha^(-1) M g_H M^(-1),
    D_red=alpha M D_H M^(-1),
    g_lit=alpha^(N-1) M g_H M^(-1),
    D_lit=alpha^(1-N) M D_H M^(-1).             (2.4)

Thus their physical normal derivatives differ:

    D_phys(g_red)=-g_red, D_phys(D_red)=D_red,
    D_phys(g_lit)=(N-1)g_lit,
    D_phys(D_lit)=-(N-1)D_lit.

Both products are exactly e and horizontal. The adapter U and
its first derivative remain part of a comparison of the two lifts;
the common root value does not identify their normal phases.
The full external d_N(M) line is unchanged and remains distinct
from this internal U normal.

The underlying full quantum modules are not identified: for example
the uncorrected cyclic operator (1-A)S^(-1) has N-th power 1-U,
whereas the root balanced head F has N-th power zero. The map
(1.1) does not suppress that endpoint source or claim to intertwine
these two different F actions.

## 3. An explicit relative source-chain map with endpoint U

Use an independent source-centralizer coordinate sigma with marked
endpoints zero and one. Keep it distinct from any physical geometric
framing parameter. On Fhat-valued series define the twisted relative
complex

    P=H[sigma][[t]],
    R_T^1=P,
    R_T^2=P direct_sum Fhat direct_sum Fhat,
    delta_T h=((partial_sigma-T)h,h(0),h(1)).

Every t coefficient in P is polynomial in sigma; endpoint
evaluation and antiderivation are therefore defined coefficientwise.
The t-adic completion permits exp(sigma T) while retaining those
endpoint maps. Conjugation by exp(sigma T), with exp(T) at
the second endpoint, identifies this complex with the ordinary
relative source complex. Its transgression is

    L_T(a,b_0,b_1)
       =integral_0^1 exp(-sigma T)a(sigma)dsigma
                                -exp(-T)b_1+b_0. (3.1)

The inclusion is f |->(exp(sigma T)f,0,0). Both identities
L_T delta_T=0 and L_T i_T=I follow by differentiating
exp(-sigma T)h(sigma). They hold before applying any cut.

Applying M coefficientwise gives a strict isomorphism to the
whole-normal complex

    delta_U h=((partial_sigma-Log U)h,h(0),h(1)),
    L_U(a,b_0,b_1)
       =integral_0^1 U^(-sigma)a(sigma)dsigma
                                    -U^(-1)b_1+b_0.           (3.2)

The coherent inclusion becomes f |->(U^sigma f,0,0).
The endpoint carry is literally U. It has not disappeared through
specialization of A^N=1. The whole averaged co-source and its
residue realization from (2.1) commute with this chain map. The
original finite cut is obtained after evaluation U=1; its normal
derivative requires the extra row (2.2), rather than a horizontal
vacuum assumption.

There is also an exact compatible normal connection on the entire
relative complex. On degree one it is B-sigma. On degree two it
is (B-sigma,B,B-1). These commute with delta_T because

    [B-sigma,partial_sigma-T]=0.

Under M they are (nabla-sigma) and
(nabla-sigma,nabla,nabla-1), respectively. Transgression carries
them to B and nabla. Using bare B without the sigma term would
give curvature -I and would be incorrect. This is an explicit
Heisenberg normal/source complex, not a conditional lifting argument.

## 4. The logarithmic torsor is necessary, not a finite-cover choice

The completed map (1.1) has a global version only after adjoining
the marked logarithmic torsor of U. On any simply connected marked
sheet, nabla(Log U)=1 and all formulas above are actual functions.
Changing the logarithm shifts its additive torsor coordinate.

There is a sharp obstruction to replacing it by algebraic functions.
Suppose a linear comparison into the algebraic whole-normal field,
or any finite algebraic cover, intertwines B with nabla and carries
some vacuum h to a nonzero horizontal value c. Since B(Th)=h,
its image f would satisfy

    U partial_U f=c.

After applying a constant component functional if necessary, c is
a nonzero constant. Thus df=c dU/U. At a zero or pole of U on
the normalized compact curve, its right side has nonzero residue.
An exact differential of an algebraic function has zero residues.
Finite covers multiply that residue by a positive ramification
index and cannot remove it. This contradiction proves that no
such nonzero vacuum/cut-preserving algebraic linear map exists.

The obstruction already appears on the first excited Fock vector;
it is not an asymptotic or high-jet problem. It also does not
contradict (1.1): Log U is a valid formal function at U=1.
The required common object is a marked logarithmic differential
torsor, rather than only a finite algebraic source cover. It can be
presented as the algebraic bundle with coordinate t and connection
dt=dU/U; the obstruction is to an algebraic horizontal section,
not to the existence of that bundle.

## 5. Relation to the actual two-dimensional divided-adjoint orbit

The explicit divided-adjoint source orbit and its marked geometric
framing chart are proved in
[the framing-orbit note](divided_source_framing_orbit.md). With its
coordinates v=a Ubar+bW, z=a+b, the map is

    r=a/z, s_geo=z^(-2),
    A_cut=z^2/(1+z^2), tau_geo=r/s_geo=a z,
    Omega_cut=d tau_geo wedge dlog A_cut.         (5.1)

This establishes an explicit bare group/form comparison. It does
not identify the source-relative sigma in Section 3 with tau_geo
at the physical quantum scale. If u=Log U=N Log A_cut, then

    Omega_cut=(1/N)d tau_geo wedge du.

At H_N=2pi*i/N, a geometric Fourier phase
tau_geo Log A_cut/H_N is tau_geo u/(2pi*i). Matching it with
the source kernel exp(s_Fock u) would therefore require
s_Fock=tau_geo/(2pi*i), changing the unit source endpoint U to
U^(1/(2pi*i)). A marked residue/phase adapter is required before
claiming such a physical polarization identity.

There is also a direct source-collapse limitation. On a diagonal
cut matrix C the normalized raw orbit insertion is

    Phi(Cv)/Phi(v)
       =(a/z)/(N-1) sum_(j<N-1) C_jj+(b/z)C_(N-1,N-1).

It depends only on a/z. Thus the two orbit parameters do not by
themselves become two independently measured internal framing
coordinates of the scalar partial knot state. The whole-normal
and relative current data above are necessary to retain the
additional direction before collapse.

## 6. What is new here and what remains

The earlier first-quantum-normal and source/monodromy notes give
the actual module/cokernel connection, its source, and the normal
lattice cut. The relative-framing note realizes the finite boundary
cut as a residue complex. They do not contain the explicit Fock
Mellin map (1.1), its endpoint-U relative chain map (3.2), or the
global algebraic obstruction in Section 4.

Those maps now compare the actual Fock and whole-normal boundary
objects directly, retaining both the reduced pivot lift and literal
clock-power lift with their exact U adapter, the distinct finite-
vacuum cut row, and every endpoint factor.
They do not prove that a computed geometric Gaussian class has
the original selected image under this map. Its extension through
the actual source boundary, the physical 2pi*i adapter and global
period coefficient remain separate requirements. No regulator
volume identity is inferred.

[Exact audit](../experiments/audit_fock_cyclic_normal_mellin_map.py).
[Results](../experiments/fock_cyclic_normal_mellin_map_results.json).
[Independent Mellin and Green audit](fock_mellin_and_green_independent_audit.md).
