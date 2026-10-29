# Meridian transport on the cut source and its geometric dual

Research note, 26 October 2026. The comparison in
[the cut-wall note](cut_wall_and_cyclic_source.md) matched source
presentations over S=C[[u,h]]. Here their normalized presentations
are compared with meridian transport included. The geometric
source has the inverse marked longitude character, which is
retained explicitly.

The result concerns the actual local cut coefficients and a
calibrated formal geometric cyclic model. It does not identify
the full knot's affine source, selected section, or volume norm.

## 1. The full actual cut has a difference-constant normalization line

Keep q=q_N=exp(pi*i/N), x=-M/q, Y=M^2, U=M^(2N), and
sigma(M)=qM. Define

    p=q^(-1)M^2-qM^(-2), r=sigma(p),
    c_2=q^2+q^(-2).

The actual two-factor modified cut in the previous note is

    Phi_N(f)=C_N(U)[r f_+ + p f_-],
    C_N(U)=-zeta_N U/[(U-1)(U+1)],
    zeta_N=q^(N(1-N)/2).                           (1.1)

Thus C_N=Gamma_N/d in that note. It is not Gamma_N that is
meridian-constant: the geometric gap d is not constant.
At an actual root sigma(U)=U, so sigma(C_N)=C_N exactly.
The physical normalization is a marked meromorphic constant
line, including its central lattice and both poles. It is not
declared a unit at U=1 or absorbed into a coefficientwise formal
unit. All statements below about regular S-presentations concern
the normalized coefficients, with this line kept separately.

The elementary exact identity

    sigma^2(p)=c_2 sigma(p)-p                     (1.2)

follows by expanding its two monomials. It provides a fixed
transport matrix for the cut coefficients:

    J=[ c_2  1 ], w=(r,p),
      [ -1   0 ]
    sigma(w)=w J, det J=1.                       (1.3)

These identities are rational in q,M; they require no formal
approximation. At roots they describe the actual weights before
any node specialization.

## 2. The wall presentation is meridian-equivariant

Work now over S with q=exp(h), M=exp(u), sigma(u)=u+h.
Give S^2 the semilinear operator T=J sigma and S the operator
sigma. The exact sequence of underlying S-modules is

    0 -> S --j--> S^2 --ell--> S -> S/m -> 0,
    j=(p,-r)^t, ell=(r,p), m=(p,r)=(u,h).          (2.1)

Every arrow intertwines its stated meridian transport. Indeed

    J sigma(j)=j, ell J=sigma(ell).               (2.2)

The first identity uses (1.2); the second is (1.3). Consequently
the normalized point source in (2.1) has character 1. This is a
specified semilinear presentation, not just an isomorphism of
point modules. Tensoring its cut with the recorded C_N line
preserves equivariance on its original root meridian chart.
Its polar specialization remains a whole-germ operation.

The ordered scalar source residue stays fixed under the base
meridian change:

    Res du dh/[p sigma(p)]
       =Res du dh/[sigma(p) sigma^2(p)]=1/16.      (2.3)

One direct verification is that the transformation of the two
equations in (1.2) has determinant one. Equivalently their two
Jacobian determinants at u=h=0 both equal 16. Also
sigma(du wedge dh)=du wedge dh. These are statements about the
base residue; a tensor period line has its own character.

## 3. The geometric cyclic free presentation has an exact shift matrix

Let a,b be the calibrated geometric ratios from the preceding
note, so

    a-b=v p, v in S^times,
    a(0,0)=b(0,0)=L_c, v(0,0)=kappa/4.

Keep the actual SL2 longitude sign L_c; it is not set to one.
On the normalized split module V=S^2 use T=diag(a,b)sigma,
e=(1,1), f=(1,0), and

    Lambda=S e direct_sum m S f.

Its generators e,pf,rf give the free presentation

    0 -> F_1 --R--> F_0 --E--> Lambda -> 0,
    R=(0,r,-p)^t,
    E=[ 1 p r ],
      [ 1 0 0 ]

with the following semilinear transports:

    T_(F_1)=a sigma,
    T_(F_0)=B sigma,
    B=[ b  0    0  ],
      [ v  0   -a  ],
      [ 0  a  a c_2].                            (3.1)

These are automorphisms: det B=b a^2 is a unit. Direct
multiplication proves both compatibility identities

    E B=diag(a,b) sigma(E),
    B sigma(R)=a R.                              (3.2)

The first uses a=b+vp, and the second uses (1.2). Thus the
single relation is itself a meridian line, with ratio a. This
records information that an S-module presentation alone omitted.

## 4. Dualizing gives exactly the cut complex with a period-line twist

For a semilinear free module T=C sigma, its S-dual transport
is C^(-t) sigma. This follows directly from

    (T phi)(z)=sigma(phi(T^(-1)z)).

The dual of (3.1) is therefore the two-term presentation

    [F_0^vee --R^t--> P_a^vee],

where P_a denotes the line with ratio a. Its degree-one
cohomology is Ext^1_S(Lambda,S). The explicit dual matrix is

    B^(-t)=[ 1/b  -c_2 v/(ab)  v/(ab) ],
           [  0       c_2/a       -1/a ],
           [  0        1/a          0  ].          (4.1)

Its first coordinate line is stable, has ratio b^(-1), and
maps to zero under R^t. It is exactly P_b^vee: as a functional
on V it kills f and sends e to one. Hence this zero column may
be quotiented out as a difference submodule, not just deleted
from an underlying linear presentation.

Define the constant quotient map

    Q=[ 0 1  0 ],
      [ 0 0 -1 ].

Then the full matrix identities are

    Q B^(-t)=a^(-1)J Q,
    R^t=(r,p)Q.                                  (4.2)

They prove an isomorphism of quotient difference complexes:

    [F_0^vee -> P_a^vee]/P_b^vee[0]
       = P_a^vee tensor [S^2_(J sigma) --(r,p)--> S_sigma]. (4.3)

Thus the normalized actual cut presentation is precisely the
universal factor of the geometric dual cyclic presentation;
the dual geometric period line is the remaining factor. All
arrows and meridian matrices are specified by (4.2).

Taking degree-one cohomology gives the equivariant comparison

    Ext^1_S(Lambda,S)=P_a^vee tensor S/m,
    T on the point = L_c^(-1).                   (4.4)

The scalar base residue remains (2.3). Multiplication by the
two units v,sigma(v) changes it to 1/kappa^2 in the calibrated
geometric equations. The opposite sign from the two ordered
density values -p,r remains the sign already recorded in the
cut-wall note. Neither that sign nor L_c^(-1) is absorbed into
zeta_N. This closes the local equivariance calculation for the
normalized cut and the calibrated geometric cyclic model.

## 5. The original root matrices check this transport

The calculation has a direct check on the original root model.
For V_x tensor V_x its generic highest roots are

    z_j=x^2 Q^(-j), Q=q^2, 0<=j<N.

The actual full projector cuts, proved from the pivotal matrices,
are d_(z_j). Substitution of the original modified dimension gives

    d_(z_j)=C_N(U) p_j,
    p_j=q^(-2j-1)M^2-q^(2j+1)M^(-2),
    sigma(p_j)=p_(j-1 mod N).                    (5.1)

Here p_0=p and p_(N-1)=r. The actual highest-vector meridian
matrix G=H(qM)P H(M)^(-1) intertwines total E,F,K and gives
the full affine crossing identity with source
(1+U^(-1))E_(N-1). Its label cycle induces exactly (5.1).
Thus (1.3) describes the cut weights under this original
meridian comparison, not only a chosen model shift on functions.

There is a useful specialization qualification. For N>2 the
free wall matrix has J^N=I, since its distinct eigenvalues
are q^2,q^(-2). At N=2 they coincide; J^2 is not identity.
The actual cut then has r=-p and its image is nevertheless
N-periodic. Its extra kernel must be retained. The formal free
presentation near q=1 is not thereby a free periodic root module
at every distant root. No new topological invariant is inferred.

## 6. The universal part of every tensor cut uses two Fourier moments

The existing intrinsic cut formula also identifies its universal
coefficient part for arbitrary strand count b>=2. At generic color
the final highest roots are z_j=x^b Q^(-j), and an actual
intertwiner has multiplicity-block traces A_j. Put

    C_b=-zeta_N/[x^(bN)-x^(-bN)],
    J_+(A)=sum_j Q^(-j)Tr A_j,
    J_-(A)=sum_j Q^j Tr A_j.

The full original cut is exactly

    mathfrak_t_W(A)=C_b[q x^b J_+(A)
                              -q^(-1)x^(-b)J_-(A)]. (6.1)

This follows by substituting the modified-dimension numerator
in the already proved full trace formula. It reduces the cut
coefficients to at most two Fourier moments. It does not reduce
the N-dimensional trace quotient or the knot's quantum-A module
to dimension two. The block traces still depend on the entire
braid and its centralizer transitions.

There is also an exact parity statement. Since sigma(x)=qx and
q^N=-1,

    sigma(C_b)=(-1)^b C_b.

Every fixed-label weight d_(z_j), as a rational function of M,
therefore satisfies

    [T^2-(-1)^b(q^b+q^(-b))T+1] d_(z_j)=0.        (6.2)

For even b the common frame is meridian-constant; for odd b
its sign line remains. For even b the actual fusion labels
also permute under the known meridian atlas. No generic
EFK-module comparison for odd b is being asserted by (6.2).
Individual Fourier moments can be polar in a singular fusion
frame, so (6.1) must still be specialized as a whole.

## 7. Scope, coverage and checks

This supplies an exact semilinear local source presentation and
its comparison to the geometric dual cyclic model, with the
marked period character and the actual normalization line kept.
The earlier all-orders normal-block comparison can transport
P_a to the dual of the corresponding actual formal normal line.
It does not identify that line with the selected finite sum.

The actual global source arrows, knot section, and central lattice
at U=1 still have to be transported through sewing. The pole in
C_N is genuine difference-constant period data; its cancellation
cannot be inferred from a regular S-unit gauge. Nonzero pairing
of the selected source with the geometric block, and its regulator
norm across levels, remain unproved. In particular this note does
not establish the global affine comparison equation for c_K,c_T.

Modified-trace and formal difference-equation coverage is the
existing coverage recorded in the preceding notes. No novelty
claim is made for free resolutions, semilinear duality, or cyclic
presentations. All displayed intertwiners and coefficient identities
are proved by the direct calculations above.

[The audit](../experiments/audit_equivariant_cut_source.py) checks
the universal wall transport, relation transport, full free cyclic
matrix, dual, stable branch line, quotient chain map and residue.
Twelve generic original root cases at N=2,3,4,5,6,9 construct the
actual E,F,K, original crossings and meridian matrices. All 116
projector cuts at both colors agree with (5.1); the full affine
crossing identity and retained normalizer are checked. The N=2
extra kernel is recorded, not treated as periodicity of its free
presentation. Four exact symbolic width checks retain the parity
in (6.2). [Results](../experiments/equivariant_cut_source_results.json).

Reproduce with:

    python3 experiments/audit_equivariant_cut_source.py

The subsequent [sewn-source theorem](sewn_source_and_meridian_charge.md)
now transports the actual residue through arbitrary full knot
operators and gives a regular rational lift of its projective
corner. It also forces a further marking: one surviving meridian
must carry charge three. Its step and full dimension factor are
retained. The inverse complete longitude character above cannot
distinguish that odd charge from charge one. The entire source
and its selected geometric period still need comparison.
