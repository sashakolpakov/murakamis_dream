# The cyclic dilogarithm, its factorial lattice and its cut-source torsor

Research note, 26 October 2026. This identifies the actual finite
factorial with a singular frame of the literature cyclic dilogarithm,
constructs its flat two-direction source extension, and computes
the complete affine transport when its cut is moved. The internal
center, meridian norm and full ADO dimension remain functions until
whole specialization. The proof is uniform in N, including even
and composite levels.

This supplies local relative data for the selected-source comparison.
It does not identify a finite factorial model with a topological
invariant on arbitrary geometric triangulations, or establish the
selected Bloch-regulator norm. The actual invariant remains the
prescribed reduced ADO evaluation F_N and its Kashaev value F_N(1).

## 1. The same local quantum function in two frames

Fix N>=2, Q a primitive N-th root, and h,nu with

    nu^N=1-h^N.

Initially assume h nu !=0. For a=0,...,N-1 put

    p_a(h)=product_(r=1)^a(1-Q^r h),
    phi_a(h)=nu^(-a) p_a(h).                         (1.1)

Then, with indices taken cyclically,

    phi_(a+1)=(1-Q^(a+1)h) phi_a/nu, phi_0=1.       (1.2)

For a<N-1 this is the factorial recurrence. At the last step,
(1-h)p_(N-1)=1-h^N=nu^N, which proves the same equation.
All its multipliers are units on this punctured Fermat cover.
Their product is one; (1.2) uniquely fixes the pointed primitive.

For comparison with a literature definition, let

    D_N(x;Q)=product_(k=1)^(N-1)(1-Q^k x)^(k/N).

Taking compatible N-th roots, cancellation of neighboring factors
gives

    D_N(Qx)/D_N(x)=(1-x)/(1-x^N)^(1/N).

Consequently the cyclic dilogarithm with that compatible root choice
has the exact normalized values

    phi_a(h)=D_N(Q^(a+1)h;Q)/D_N(Qh;Q).             (1.3)

This is an equality of the pointed cyclic primitives, not a limit
formula. Their N-th powers already agree as rational products;
(1.2) selects the coherent roots. Equivalent conventions insert
the usual argument shift, inverse or common power of 1-h^N.
Thus (1.1) reconstructs an existing quantum definition rather than
introducing a replacement local quantum function.

The root tetrahedron module is literal here. On functions of
a modulo N let

    (Xf)_a=Q^(a+1)h f_a,  (Y_op f)_a=nu f_(a+1).

Then XY_op=Q^(-1)Y_op X and

    (X+Y_op-1)phi=0,
    X^N=h^N, Y_op^N=1-h^N.                          (1.4)

After reversing the index a, these are precisely the clock/shift
matrices and the normalized kernel of
[the pointed tetrahedron construction](pointed_tetrahedron_gluing.md),
with s=Qh, t=nu and R=Q^(-1).

## 2. The actual boundary is a lattice, not an evaluation of phi

Multiply component a by nu^a. The vector p of (1.1) extends
polynomially to h=1, nu=0 and has

    p_a(1)=(Q;Q)_a !=0, 0<=a<N,
    p_(N-1)(1)=N.                                  (2.1)

The last equality follows by evaluating
product_(r=1)^(N-1)(1-Q^r h)=(1-h^N)/(1-h) at h=1.
The diagonal frame diag(1,nu,...,nu^(N-1)) is singular there.
The cyclic vector phi generally has poles of orders a on this
cover; its rescaled factorial lattice has the stated regular value.

The reciprocal primitive 1/p_a is also regular at h=1. These are
the factorial and inverse-factorial frames used in the actual cut
state. Products with meridian-dependent factorials must first be
compressed to their finite Pochhammers when an individual quotient
has a pole. The Laurent-polynomial crossing identity supplies
that continuation; separate singular factors are not evaluated.

Thus a nondegenerate geometric tetrahedron and the Kashaev cut
boundary lie in different parts of a common relative family.
Their fixed central characters have not been identified.

## 3. Retain the internal center and its chosen cut root

Let C=theta^N, U=Y^N, and use the finite etale algebra

    S=K(Y,theta)[t]/(t^N-C).

Its marked components are t=theta Q^a. There are two commuting
base shifts:

    sigma(t)=Qt, sigma(Y)=Y;
    delta(Y)=QY, delta(t)=t,

with theta fixed in both. Put h=Y theta and interpolate p_a(h)
as p_theta(t;Y). Let e_partial be supported at t=theta Q^(-1),
and e_0 at t=theta. Directly from the finite products,

    sigma p_theta=(1-QYt)p_theta+UC e_partial,
    delta p_theta=(1-QYt)p_theta/(1-QYtheta).         (3.1)

The first equation includes the last transition; its defect is
1-(1-h)p_(N-1)=h^N=UC. The second is the cancellation of
p_a(Qh)/p_a(h). Both are identities of whole finite primitives.

The homogeneous, uncut factorial recurrence in the free variable
t has meridian multiplier

    a_Y=(1-QYt)/(1-QY).

It is the generic recurrence normalized at index zero before
imposing an internal periodicity. This normalization is fixed by
p_a(Y)=(QY;Q)_a, not selected to impose a desired central curve.

## 4. Flatness forces a source line with a nontrivial norm

Seek an extension retaining the bulk multipliers and source in
(3.1), with no off-diagonal meridian source in this frame. Its
two matrices must be

    B_sigma=[ 1-QYt   UC e_partial ],
            [   0          1      ]

    B_delta=diag(a_Y,d_Y),
    d_Y=(1-QYtheta)/(1-QY).                         (4.1)

Here the source line has sigma=1 and delta=d_Y. The source
multiplier d_Y is forced: flatness in the top-right entry requires

    sigma(a_Y) UC e_partial=delta(UC e_partial) d_Y.

The source and UC are delta-invariant. On its support,
sigma(a_Y)=(1-QYtheta)/(1-QY), giving exactly d_Y. The bulk
entry also satisfies sigma(a_Y)(1-QYt)=delta(1-QYt)a_Y.
Therefore

    sigma(B_delta) B_sigma=delta(B_sigma) B_delta.   (4.2)

This is a genuinely flat two-direction difference extension.
The diagonal source line is the norm torsor

    Norm_delta(d_Y)=(1-UC)/(1-U)=:V.                (4.3)

The same norm holds for a_Y since t^N=C. At a free internal
center this norm need not be one. Setting C=1 first makes it
one and removes precisely that varying-center information.

The complete monodromies can be read without a determinant:

    B_sigma,cyc=[ 1-UC   UC p_theta ],
                [   0        1     ]
    B_delta,cyc=V I_2.                             (4.4)

Indeed the internal bulk product is 1-UC and its distinguished
fixed vector is (p_theta,1). The meridian product is diagonal
and both diagonal products equal (4.3).

One may express the pointing without making a false rational
horizontal-frame assertion. Take a source generator g with
sigma g=g and delta g=d_Y g. Then

    g (p_theta,1)^T

satisfies both matrix equations (4.1). At theta=1 the source
line has d_Y=1, and g=1 is the actual finite-factorial pointing.
At a general C its meridian norm is V, so g cannot be replaced
by the same rational constant.

## 5. Exact affine transport when the cut root changes

Keep t and C fixed and change theta to theta'=Qtheta. A product
cancellation, including the cut component, gives

    (1-QYtheta) p_theta'=p_theta-UC e_0.             (5.1)

Away from e_0 it just drops the first factor of p_a. At e_0
its left side is 1-UC, whereas p_theta=1, proving the correction.
The full, unnormalized cut adapter is therefore

    J_raw=[ 1  -UC e_0 ],  H=1-QYtheta.             (5.2)
          [ 0     H    ]

It takes (p_theta,1) to H(p_theta',1). Substitution in (4.1)
gives, for both shifts tau=sigma,delta,

    tau(J_raw) B_tau,theta=B_tau,theta' J_raw.       (5.3)

Thus the source term and its pointing are transported together.
The source-line ratio is d_Y,theta'/d_Y,theta=delta(H)/H,
an explicit Hilbert-90 comparison.

After N successive cut moves the root theta returns. The entire
adapter, however, has loop

    J_raw,loop=[ 1  -UC p_theta ],                  (5.4)
               [ 0     1-UC    ]

not an overall scalar multiplier. To prove it, put
G_theta=[[1,p_theta],[0,1]]. Then

    J_raw=G_theta' diag(1,H) G_theta^(-1).

The G factors telescope and product H=1-UC. This proves (5.4)
uniformly. Treating a source transport as only its scalar
determinant would lose this off-diagonal term.

## 6. Coherent transport on the Fermat root cover

Retain nu^N=1-UC and nu!=0. With the homogeneous comparison
fixed to the identity, define

    J=G_theta' diag(1,H/nu) G_theta^(-1).            (6.1)

The factor H/nu has delta-norm one. It obeys the same two
intertwining equations and takes (p_theta,1) to
(H/nu)(p_theta',1). Every N-step cut loop is now exactly the
identity, since product H=nu^N. This is strict local cut-root
descent of the extension and its source pointing on the stated
cover. Changing the chosen nu records a mu_N character.

Dividing the entire J_raw by nu gives a different answer:
its N-loop is G_theta diag((1-UC)^(-1),1) G_theta^(-1), not
the identity. The source channel must be normalized as in (6.1);
an arbitrary common multiplier is not equivalent to that operation.

At nu=0 the normalized adapters can have poles. They are not
evaluated separately at that divisor. A finite collection of
cuts admits a lattice stable under this finite cyclic transport:
on their direct sum take sum_(r=0)^(N-1) J_total^r Lambda_0.
This is a finite fractional lattice because J_total^N=1; over
a normalized curve it is torsion free and hence locally free.
The construction retains the poles and the pointing. It makes
no assertion that individual adapters have a regular invertible
matrix in the original factorial frame at the degenerate point.

## 7. The full ADO factor is a specified endpoint transport

On the actual cut theta=1, the raw source-line transport through
N-1 successive roots is

    product_(r=1)^(N-1)(1-Q^rY)=S_N(Y)
         =(1-Y^N)/(1-Y).                            (7.1)

At q=q_N, Y=M^2, the full modified dimension is exactly

    d_N(M)=eta_N M^(N-1)/S_N(Y), eta_N=i^(N+3).      (7.2)

Thus its nonmonomial factor is the inverse raw endpoint
transport of this actual source line. In the coherent frame
(6.1) the same endpoint transport is S_N(Y)/nu^(N-1).
Recovering (7.2) requires the compensating factor nu^(-(N-1));
discarding it loses the original boundary germ. Their whole
ratio specializes to 1/N at Y=1.

The meridian gauge remains exactly

    d_N(qM)/d_N(M)=-q^(-1)(QY-1)/(Y-1),
    Norm_delta(d_N(qM)/d_N(M))=(-1)^(N-1).          (7.3)

The q convention and phase eta_N are unchanged; a Q-only local
formula is not permission to remove this full-state sign.

## 8. Tensor sources retain every wall intersection

For finitely many factors with sigma f_j=a_j f_j+b_j s_j,
where s_j is the source component, the exact product equation is

    sigma product_j f_j=(product_j a_j)(product_j f_j)
      +sum_(nonempty S) (product_(j in S) b_j s_j)
                         (product_(j not in S) a_j f_j).       (8.1)

This is the top entry of the tensor of their rank-two extensions.
It retains the face and corner sources. For example at two
factorial cut walls with s_1=s_2=1 and h_1=h_2=1 the bulk multipliers both
vanish and both b_j equal one. The b_1 b_2 corner supplies the
entire shifted product one; deleting it gives zero.

The tensor source quotient retains its lower tensor factors and
their source lines. In a meridian direction those lines carry
the norms (4.3). They are not all replaced by one trivial quotient
before the actual relative pushforward is proved.

Commuting shift pullbacks and tensoring preserve flatness by
(4.2). In a finite tensor contraction with specified dual
pairings, use J on a transported leg and its dual inverse on
the paired leg. Interior adapters cancel exactly; the marked
boundary vectors and evaluation functional must also move.
This is an algebraic transport theorem for an already specified
network. It does not assign such a network to every ideal
triangulation or prove all its Pachner and turn relations.

## 9. The actual crossing is retained, not redefined

The actual positive and inverse crossings use the Gaussian
factorial at Q and the color primitive

    H_a(M^2)=(Q^(-1)M^2;Q^(-1))_a.

For example the positive finite Pochhammer equals

    (Qx^2/Q^a;Q)_k=H_a(M^2)/H_(a-k)(M^2), M=-qx.

The Gaussian binomial is p_a(1)/(p_k(1)p_(a-k)(1)). These
are exactly the regular factorial lattices of Section 2, in
the two orientations. Substituting them in the independently
derived crossing formulas gives every original matrix entry,
including its Gaussian power, sign and endpoint support.
At exceptional parameters cancel to the finite product first.
Hence every finite cut contraction, with its original pivot
and twist, is exactly the same actual ADO period. This local
equivalence neither repairs the earlier positive factorial
model's failed 2-to-3 test nor supplies a new knot invariant.

The new relative data identify how the actual factorial cut
can be included in a cyclic tetrahedron family with its source,
cut-root cover and normalization. A global transport to the
positive geometric triangulation must preserve this whole
object and establish its nonzero geometric coupling. The
selected regulator norm is still unproved.

The internal shift sigma and meridian shift delta have been
distinguished throughout. This level-N factorial family is not
being identified with the companion of the actual all-level
meridian annihilator. In particular (4.3) is a local source-line
norm, not an asserted factor of that operator's spectral curve.

The subsequent [common carry-lattice theorem](carry_recoupling_lattice.md)
now controls the complete factorial contraction of arbitrary
finite recoupling trees at simultaneous degeneration. Its poles
are exactly the integer carries floor(sum i_j/N), and its image
lattice is independent of the tree. Local moves preserve the
actual sublattice and the full cut functional. A wrapped crossing
lift retains the wall sources and has exactly the original ADO
cut trace at every meridian color. This resolves integral
recoupling for that presentation; assignment to an arbitrary
positive geometric triangulation and the selected regulator
norm remain additional comparisons.

The subsequent [controlled cyclic Euler-source calculation](controlled_cyclic_euler_source.md)
now gives another exact frame of this same factorial source.
The coefficients of the existing determinant-normalized cyclic
dilogarithm are a reflected phase transform of p_a(nu), multiplied
by the specified scalar gamma_N. The entire cyclic source equation,
local argument shift and co-source transform with it. A norm product
fixes gamma_N, and a direct estimate bounds it and its inverse by
powers of N on marked compact charts. Its source value is 1/N;
the complete ADO phase remains eta_N. The mixed central pentagon
retains its corner source. These are local fixed-root source
comparisons; they do not identify the global meridian quantum-A
extension or its selected geometric period.

## 10. Literature coverage and independent diagnostics

Cyclic quantum dilogarithms on Fermat covers are established
definitions. The finite-product definition and shift convention
are covered by
[Ip--Yamazaki, 1412.5777](https://arxiv.org/abs/1412.5777),
Definition 3.3, including its displayed alternate normalization,
and the original Kashaev framework already cited in
[the Verma transport note](verma_tetrahedral_transport.md).
No published pentagon or state-comparison proof is used here.
All the source, lattice and adapter formulas follow from the
finite products (1.1).

For coverage of the need for lifting data, Ishibashi's
[16 October 2026 correction, 2610.23572v1](https://arxiv.org/abs/2610.23572v1)
states additional mu_N data and a general pentagon phase.
Only its abstract was checked. Our N-step cut identity (6.1)
is independently proved; it is not a proof that a global
pentagon phase or geometric source comparison is settled.

[The exact audit](../experiments/audit_factorial_source_torsor.py)
checks both flatness directions, both cyclic monodromies, the
raw affine adapter, its non-scalar loop, and the strict normalized
loop at N=2,3,4,5,6,8,9,10,12. It compares the cyclic primitive
with the independent tetrahedron kernel and with N-th powers
of the literature finite product. Eight tensor-wall tests check
the necessary corner sources. It reconstructs 6,876 actual
positive/inverse entries, 18 closed cut periods, and the entire
modified dimension, including generic and Kashaev colors.
All passed. Results:
[factorial_source_torsor_results.json](../experiments/factorial_source_torsor_results.json).

    python3 experiments/audit_factorial_source_torsor.py
