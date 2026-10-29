# The actual regular figure-eight connection and regulator-fixed channels

28 October 2026. This tests the majorization criterion on the ACTUAL
regular affine figure-eight quantum-A packet, rather than on the
already excluded positive pivotal trace of the original crossing.
The natural instantaneous modal connection is not a scalar multiple
of a unitary. Its polar unitary is bistochastic but does not fix the
geometric regulator observable. The same failure occurs inside the
macroscopic source tail at Y=-i, not only at Y=i.

This is a local statement in a specified classical eigenframe. A
superadiabatic change of frame can remove the first-order off-diagonal
terms; no impossibility of a different global source-retaining
connection is asserted.

## 1. A pure amplitude map cannot be silently made bistochastic

Let C be an invertible square matrix. Suppose a completely positive
trace-preserving map Phi has, for every pure input psi, a pure output
on the line C psi. Then C^*C is a scalar matrix, and Phi is the
corresponding unitary channel. This includes a claimed equality with
C psi psi^* C^* up to one common scalar, as well as the normalized
pure-output prescription.

Proof. Write Phi(X)=sum_a K_a X K_a^*. Positivity and the rank-one
output imply K_a psi is on the line C psi for every psi and a.
Thus C^(-1)K_a preserves EVERY vector line. Applying it to basis
vectors and their pairwise sums gives C^(-1)K_a=c_a I.
Trace preservation yields (sum|c_a|^2)C^*C=I. Since C is square,
its scalar normalization is unitary; unitality follows as well.

Agreement on ONE selected pure state is much weaker and does not
imply this conclusion. Introducing a dephasing, a Kraus completion,
or a state-dependent postselection normalization changes the original
coherent map unless the extra source contributions are retained.

## 2. Exact original connection and its normalized eigenframe

Use the exact coefficients and original source of
[the actual regulator-weighted transfer](actual_regulator_weighted_a_transfer.md):

    w_(j+1)=T_Q(Y)w_j+f_Q(Y), Q=exp(i tau), tau=2pi/N,
    T_Q=[-c0/c+, -c-/c+; 1,0], f_Q=(D/c+,0)^t.

No affine source is set to zero in this note. In a classical modal
frame S(Y) its exact update is

    z_(j+1)=K_N(Y)z_j+g_N(Y),
    K_N=S(QY)^(-1)T_Q(Y)S(Y),
    g_N=S(QY)^(-1)f_Q(Y).                         (1)

On a hyperbolic interval put

    P=Y^2+Y^-2-Y-Y^-1-2, lambda+lambda^-1=P,
    V=[lambda,lambda^-1;1,1], Lambda=diag(lambda,lambda^-1).

Choose the real negative expanding root lambda<-1 and normalize
EACH eigenvector column in the Euclidean norm:

    S=V diag(n1,n2),
    n1=(lambda^2+1)^(-1/2), n2=-lambda n1.

This is a fixed, tame modal energy convention. Its columns need not
be mutually orthogonal in the original companion coordinates.
Factor the known one-step diagonal propagation on the LEFT and
call C_N=Lambda^(-1)K_N its instantaneous connection. This is a
factorization of (1); the source g_N stays in (1) and, if the output
is divided by Lambda, must be divided by Lambda there as well.

Put s=sqrt(3). At Y=i, P=-4 and lambda=-2-s. The exact quantum
subprincipal term AND moving-frame derivative give

    C_N=I+tau E+O(tau^2),
    E=[ -5/12          (s-1)/6;
        -(s+1)/6      -5/12 ].                   (2)

Here is a direct derivation from the previously checked connection.
In the unnormalized frame V, K_N=Lambda+hB+O(h^2), h=i tau,
with B12=i(s-1)/6 and B21=-i(s+1)/6. The full first-order
matrix Lambda^(-1)iB is

    [ (s-1)/6       (3s-5)/6;
      -(3s+5)/6    -(s+1)/6 ].

Column normalization conjugates it by diag(1,2+s), and subtracts
diag(d_theta log n1,d_theta log n2). At Y=i,

    d_theta log n1=1/4+s/6,
    d_theta log n2=1/4-s/6,

since d_theta P=2. This proves every entry of (2). Omitting the
moving normalization would give different diagonal terms.

## 3. The polar test fails for the diagonal regulator observable

Equation (2) gives

    C_N^*C_N=I+tau[ -5/6  -1/3;
                    -1/3  -5/6 ]+O(tau^2).       (3)

The off-diagonal term is nonzero, so no common scalar normalization
makes this pure amplitude map unitary for all sufficiently large N.
The lemma in Section 1 excludes a bistochastic channel agreeing on
all pure inputs with this specified connection.

Its polar decomposition C_N=U_N H_N does have a unitary part:

    U_N=I+tau(s/6)[0,1;-1,0]+O(tau^2),
    H_N=I+tau[-5/12,-1/6;-1/6,-5/12]+O(tau^2).    (4)

For a nonconstant diagonal calibrated regulator R=diag(r1,r2),

    (U_N^* R U_N-R)_12
                    =tau(s/6)(r1-r2)+O(tau^2).   (5)

Thus the natural polar unitary is bistochastic but NOT
regulator-fixed. Dropping H_N is not the actual amplitude evolution.
Its off-diagonal positive part also fails to commute with R.
Both errors are polynomial, whereas the exponential action gauge
requires the stronger control in the majorization theorem.

This rotation cannot be removed by a positive diagonal rescaling of
the same classical eigenlines. Such a rescaling with ratio t>0
changes the off-diagonal generator entries to a t and -b/t,
where a=(s-1)/6,b=(s+1)/6. The polar skew entry has modulus
(a t+b/t)/2>=sqrt(ab)=1/(3sqrt(2))>0. Diagonal phase marks change
its phase but cannot make it vanish. This statement is about the
specified instantaneous eigenlines, not arbitrary nondiagonal frame
corrections.

Conjugation gives the actual SOURCE-TAIL point Y=-i, x=3/4:

    C_N(-i)=I-tau E+O(tau^2),
    (U_N(-i)^* R U_N(-i)-R)_12
                   =-tau(s/6)(r1-r2)+O(tau^2).   (6)

The geometric/conjugate figure-eight regulators are different there.
From the midpoint zero anchor they agree at x=2/3, while on
2/3<x<1 one eigenvalue has |lambda|>1 and its reciprocal has
modulus less than one. Their regulator derivatives have opposite
nonzero signs, so the gap at x=3/4 is nonzero. Hence (6) is a test
on the relevant restarted half orbit as well.

The affine source is present in BOTH modes. At either Y=i or -i,
f_0=(2,0)^t and

    S^(-1)f_0=(-sqrt(lambda^2+1)/s,
                        sqrt(lambda^2+1)/((-lambda)s))^t.      (7)

Both entries are nonzero. Neither the polar part nor a regulator
projection may be substituted into (1) without its transformed
source and the corresponding energy cross term.

## 4. An actual conserved flux, and its limitation

The exact rational functions -c0/c+, -c-/c+ and D/c+ are REAL
when |Q|=|Y|=1: conjugation Q->Q^-1,Y->Y^-1 fixes each one.
This follows by direct factor cancellation, not just at the
classical limit. On a regular arc where det T_Q>0 put

    J=[0,i;-i,0].

For every real 2 by 2 matrix T,

    T^* J T=(det T)J.                            (8)

Thus T_Q/sqrt(det T_Q) preserves this Hermitian indefinite
Wronskian form EXACTLY. Similarly C_N is real with positive
determinant, so its polar U_N is a real rotation and fixes J
exactly. This gives an actual fixed Hermitian observable, but it
is not the diagonal geometric regulator: its eigenvectors are the
circular superpositions of the two real modal lines.

The form has eigenvalues +1,-1 and provides no positive norm bound.
Moreover the actual ordinary figure-eight values and source are
real on the root orbit, so their J flux is identically zero; the
affine cross current vanishes on such real vectors too. Large real
solutions can have zero flux. This conserved observable cannot
replace the required positive regulator energy. It also does not
establish an identity on the tiny COMPLEX-q source circle.

## 5. The source-specific route remains possible

The explicit failure above does not exclude an exact global flag
after a nontrivial source-retaining change of coordinates. Already
locally an O(h) nondiagonal correction can kill the O(h) mixing:
if K=Lambda+hB, choose X_ik=-B_ik/(lambda_i-lambda_k), i!=k,
and use V_new=V(I+hX). The transformed off-diagonal starts at
O(h^2); the affine source transforms by the same inverse frame.
The previously proved analytic iteration improves this locally to
an exponentially small remainder, with an explicit action barrier.

The actual [pointed Newton--Green factorization](pointed_newton_green_barrier.md)
also supplies a stronger global source estimate for this prototype,
without proving this local bistochastic description. These tests
neither rule out nor construct a different source-selected global
flag. What does not follow from the Ward identities or the eigenvalue
curve alone is
the proposed bistochastic, regulator-fixed description in the
instantaneous classical frame: (2)--(7) are exact obstructions to
that literal claim. A global coherent/normal source reduction,
its nodal connection matrices, and their exponential costs still
need a separate proof for a broad class.

[Audit](../experiments/audit_actual_regulator_channel_test.py) verifies
the exact constants, rational reality, both actual orbit points,
polar and regulator defects, retained source components, and the
Wronskian alternative.
