# The full actual reassociation is an angle half-density

29 October 2026. Every entry of the actual adjacent-pair fusion
reassociation has a unique two-transfer path. In the source-fixing
physical quarter-factorial gauge, its squared entry is exactly a
product of FOUR positive affine-angle weights, one per cell. The full
root phase and all strict finite-head inequalities are explicit.

This is an all-entry, all-exterior tensor identity. It supplies actual
shared-charge incidence, rather than assigning independent angle
variables after taking absolute values. It does not yet identify this
cell complex with a geometric ideal triangulation or bound its global
partition by knot volume.

## 1. The actual divided-power fusion is one finite Euler operator

Put `q=exp(pi*i/N)`, `Q=q^2`, `d=N-1`, `F_a=(Q;Q)_a`,
`s_a=|F_a|`, and use the original balanced head basis. Let

    S^-|a>=|a-1> for a>0, S^-|0>=0,
    mathsfF|a>=(1-Q^(a+1))|a+1>, mathsfF|d>=0.

For a nonzero original meridian root x, divide the ACTUAL Borel
fusion column indexed `(a,b)` by its explicit `F_a`, and denote
the resulting map by C'_x. Its exact kernel is

    (C'_x)_(a-r,b+r;a,b)=x^(-r) [b+r choose r]_Q,
    0<=r<=min(a,d-b).                                (1)

All other entries vanish. This follows either from the original
coproduct powers or from the physical kernel of
[actual fusion](actual_borel_regular_fusion_and_divided_cap_period.md).
No relative index is identified with a physical one without this map.

Set `T_x=x^(-1) S^- tensor mathsfF`. Then `T_x^N=0` and

    C'_x=p_N(T_x), p_N(t)=sum_(r=0)^d t^r/F_r,
    (C'_x)^(-1)=sum_(r=0)^d (-1)^r Q^(r(r-1)/2)t^r/F_r
                                                      evaluated at t=T_x. (2)

Indeed the r-th power has coefficient `x^-r F_(b+r)/F_b`.
The finite Euler inverse follows by q-binomial convolution. Its
inverse entry is (1) times `(-1)^r Q^(r(r-1)/2)`, with exactly
the SAME strict support. Every endpoint and zero transfer is retained.

For reference the head relation is EXACT at both finite endpoints:

    S^- mathsfF=(1-Q)I+Q mathsfF S^-.

On three heads it gives `T_23 T_12=Q T_12 T_23+(1-Q)T_13`,
where `T_13=(xy)^(-1)S_1^- mathsfF_3` if the two fusion parameters
are x,y. Thus the overlap is an actual finite q-oscillator algebra,
with no silently omitted rank-one endpoint correction.

## 2. Every reassociation entry, including its phase

Let

    A_xy=(I tensor C'_y)^(-1)(C'_x tensor I).

For input `(a,b,c)` the only possible outputs are

    (u,v,w)=(a-r,b+r-s,c+s),
    0<=r<=min(a,d-b), 0<=s<=min(b+r,d-c).              (3)

For each input/output there is at most one path, since
`r=a-u`, `s=w-c`. The COMPLETE entry is

    A_(u,v,w;a,b,c)
      =(-1)^s Q^(s(s-1)/2)x^(-r)y^(-s)
            [b+r choose r]_Q [c+s choose s]_Q.         (4)

In particular the intermediate head bound `b+r<=d` is essential;
checking only the final output would add spurious entries. Formula
(4) follows by multiplying the two literal kernels (1)--(2).
It is an operator identity on the complete finite three-head space,
so it preserves ANY adjoining tensor, source or current when all
their interfaces are transported. No knot scalar occurs in it.

Assume now `|x|=|y|=1`, including the original complete source.
Write `beta_(L,r)=s_L/(s_r s_(L-r))`. The principal half-root identity
`[L choose r]_Q=q^(r(L-r)) beta_(L,r)` gives the exact unit phase

    omega=(-1)^s x^(-r)y^(-s)
                           q^[rb+sc+s(s-1)].          (5)

All signs and the half-period q are kept, at odd and even N.
There is also an exact Fourier polarization of this phase:

    omega=zeta_out(u,w) zeta_in(a,b,c) q^(-ub-wc),
    zeta_out=(-1)^w x^u y^(-w)q^(w^2-w),
    zeta_in=(-1)^c x^(-a)y^c q^(ab+c).               (5a)

Substituting `u=a-r,w=c+s` proves (5a). Its bilinear part is
a TWO-variable 2N-half-clock Fourier phase. The physical indices
still lie in the original N-windows with the strict constraints (3);
an unwindowed Fourier/Plancherel replacement is not authorized by
this phase identity alone.

## 3. Source-fixing quarter gauge and four positive cells

Use the PHYSICAL gauge

    g_a=L_a^(-1/4)=N^(1/4)/sqrt(s_a),
    L_a=s_a^2/N,
    h_a=g_a^2=sqrt(N)/s_a.

It is source-fixing because `g_a g_(d-a)=1`. The original cup and
ordinary cap are fixed on their complementary physical indices;
the full marked row has this property on its degree-d restriction.
The original integer-degree argument forces that restriction only
after the other ordinary caps have been assembled. We use exactly
that whole-source scope, as in
[the physical weighted-source theorem](actual_weighted_fourier_plat_energy.md).
Original pivots commute with this gauge. No marked corner is inserted
in an arbitrary exterior.

Let `Ahat=g^(tensor 3) A (g^(-1))^(tensor 3)`. For every entry (3),

    |Ahat_entry|^2
      = beta_(a,r) beta_(b+r,r) beta_(b+r,s) beta_(c+s,s)
      = N^4 product_(j=1)^4 w_N(alpha_j),             (6)

where `w_N(i,j,k)=1/(s_i s_j s_k)` and

    alpha_1=(r,a-r,d-a),
    alpha_2=(r,b,d-b-r),
    alpha_3=(s,b+r-s,d-b-r),
    alpha_4=(s,c,d-c-s).                             (7)

Every alpha has nonnegative integer entries summing EXACTLY to d.
The full complex half-density is therefore

    Ahat_entry=N^2 omega sqrt(product_j w_N(alpha_j)). (8)

Proof. The squared gauge ratio is
`s_a s_b s_c/[s_(a-r)s_(b+r-s)s_(c+s)]`. Multiply this by
the squared magnitudes of the two binomials in (4). Inserting the
intermediate `s_(b+r)` expresses the result as the four beta
factors in (6). Finally each beta is exactly
`N w_N(r,L-r,d-L)` by root complementation. This proves (6)--(8)
without changing or suppressing any original source factor.

For a single C'_x or its inverse, the corresponding two-cell formula
is

    |Chat'_entry|^2
       =N^2 w_N(r,a-r,d-a)w_N(r,b,d-b-r).             (9)

The inverse has the additional unit phase from (2), so its positive
cell kernel is identical, while its coherent composition differs.

### Exact incidence, rather than independent angles

The four cells in (7) satisfy

    alpha_1,1=alpha_2,1=r,
    alpha_3,1=alpha_4,1=s,
    alpha_2,3=alpha_3,3=d-(b+r).                     (10)

The external ports are recovered by

    a=alpha_1,1+alpha_1,2, b=alpha_2,2, c=alpha_4,2,
    u=alpha_1,2, v=alpha_3,2,
    w=alpha_4,1+alpha_4,2.                           (11)

Conversely four nonnegative sum-d triples satisfying (10), with
these boundary values, recover exactly one admissible entry (3).
Thus (7),(10),(11) are a bijective actual local charge model;
their five free integer parameters are `(a,b,c,r,s)`. In particular
the intermediate upper wall is the shared NONNEGATIVE charge
`alpha_2,3=alpha_3,3`. Integer total degree is conserved.

These are proven shared-spin constraints. They are not by themselves
the geometric equation that sums dihedral angles to 2pi around each
edge of an ideal triangulation. That further global identification,
including peripherals, must be established rather than inferred
from the presence of positive sum-d cells.

## 4. Exact factorization through the normalized b coefficients

This kernel is compatible with the proposed LENGTH normalization,
not an unrelated square-root replacement. Put

    B_L(X,Y)=product_(j=0)^(L-1)(X-Q^jY),
    D_L=s_L^(1/2)/N^(1/4), b_L=B_L/D_L,
    m_j=s_j/sqrt(N),
    tau_(L,r)=sqrt(m_r m_(L-r)) [X^(L-r)Y^r]b_L.

The [normalized coefficient Gram identity](actual_length_normalized_star_gram.md)
is exactly

    |tau_(L,r)|^2=sqrt(N)w_N(r,L-r,d-L),
    arg(tau_(L,r))=arg[(-1)^r q^(r(L-1))].           (12)

For one positive or inverse fusion cell let `m=b+r`. Then

    Chat'_entry=sqrt(N) eta_+ tau_(a,r)tau_(m,r),
    (Chat'^(-1))_entry=sqrt(N) eta_- tau_(a,r)tau_(m,r),
    eta_+=x^(-r)q^[r(2-a-r)],
    eta_-=(-1)^r x^(-r)q^[r(1-a)].                  (13)

For the full reassociation the exact complex coefficient is

    Ahat_entry=N eta tau_(a,r)tau_(b+r,r)
                         tau_(b+r,s)tau_(c+s,s),
    eta=(-1)^s x^(-r)y^(-s)
                        q^[r(2-a-r)+s(1-b-r)].       (14)

Multiplying the four phases in (12) proves (14), including (5).
In particular ZERO lengths are retained: `b_0=N^(1/4)` and
`tau_(0,0)=N^(-1/4)`. At the all-zero input the factor
`N tau_(0,0)^4` is one, as the original operator requires.
The b-length tensor and physical quarter gauge have therefore
been matched with their actual normalizers and source types.

## 5. Positive energies and the full coherent Gram

For a fixed input i, the exact column energy is the positive sum

    ||Ahat e_i||^2=N^4 sum_(r,s satisfying (3))
                                      product_j w_N(alpha_j). (15)

The Hilbert--Schmidt energy is its sum over all physical inputs.
Thus each local positive cell contributes ONE w, not its square.
This is a genuine identity for the entire column, not a saddle
approximation or a single selected large entry.

The FULL Gram, however, is

    (Ahat^*Ahat)_(i,j)
       =N^4 sum_(common output o) conj(omega_(o,i))omega_(o,j)
                 sqrt(W_(o,i)W_(o,j)),
    W_(o,i)=product_four_cells w_N.                  (16)

Off-diagonal replicas remain. They cannot be deleted as an exact
source operation. Any all-exterior upper comparison obtained by
Cauchy must bound or retain these mixed terms; (16) states their
phase and incidence explicitly. The original marked source has
not been assumed positive or diagonal.

## 6. The complete original crossing uses the same physical cells

There is no remaining standalone factorial diagonal between these
physical Euler maps. Let `C'_(21)=Flip C'_(12) Flip`, and retain
the original Gaussian

    D_2|a,b>=(-1)^b Q^(b(b-1)/2)x^(-2b)|a,b>.

For the original same-color braid at every meridian root x,

    R_+=kappa C'_(12) D_2 C'_(21) (C'_(12))^(-1),
    R_-=kappa^(-1) C'_(12) (C'_(21))^(-1)
                                      D_2^(-1)(C'_(12))^(-1). (17)

Here kappa is the original full common Cartan scalar, not a new
normalization. To verify (17), start with the exact all-integer-degree
factorization in [the Pascal theorem](actual_pascal_coherent_gram.md#61-an-exact-pascalgaussian-alphabet-for-original-braid-crossings).
There `C=C' diag(F_a)`. Conjugating its relative Euler factor U
by this diagonal gives coefficient
`x^-r F_(a+r)/(F_a F_r)=x^-r[a+r choose r]`, exactly the physical
C'_(21), with its strict bounds. The diagonal commutes with D_2.
This proves (17) in EVERY total degree and hence as a full operator.
The negative formula is its literal inverse.

At completeness D_2, kappa and all original pivots/framing phases
have modulus one. In the SAME source-fixing quarter gauge, each of
the three C' factors in a crossing has the two-cell kernel (9).
Their inverse phases, upper/lower walls and original finite source
remain present. This is an exact coherent physical alphabet at
arbitrary braid width, not a source-null completion or a deletion
of the inhomogeneous current.

It provides six positive cell weights per crossing before any
shared-head contractions. To turn the resulting positive comparison
into a sharp volume theorem one still needs its global geometric
edge/peripheral constraints or a further coherent contraction.
Neither is asserted merely from (17). In particular a generic
positive path partition is not automatically the partition on an
ideal geometric triangulation.

[Audit](../experiments/audit_actual_reassociation_angle_kernel.py):
original coproduct-derived fusion, finite Euler inverses, all strict
reassociation entries, half-root phases, b_0 and normalized coefficient
factorization, exact local charge incidence and both ORIGINAL signed
crossing operators with retained common Cartan.
