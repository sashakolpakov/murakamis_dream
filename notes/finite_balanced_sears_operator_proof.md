# An own finite proof of the balanced Sears transformation

29 October 2026. This proves the terminating balanced 4phi3 identity
by a finite polynomial calculation. No 6j formula, orthogonality
measure, named summation theorem or source identification is assumed.
It can be specialized to a root whenever the displayed denominators
are nonzero, since the generic identity is rational.

For generic base v and integer n>=0, let def=abc v^(1-n). Then

    sum_(k=0)^n (v^-n,a,b,c;v)_k v^k/(v,d,e,f;v)_k
      =(e/a,de/(bc);v)_n/(e,de/(abc);v)_n
       *sum_(k=0)^n (v^-n,a,d/b,d/c;v)_k v^k
          /(v,d,av^(1-n)/e,de/(bc);v)_k.             (1)

Parenthesized lists mean products of finite Pochhammers. Thus (1)
is a finite rational identity. Exceptional generic eigenvalues used
below are avoided only during its proof; they do not add a hypothesis
to a defined root specialization.

## 1. A symmetric finite polynomial operator

Choose four generic parameters A,B,C,D, P=ABCD. On symmetric Laurent
polynomials h(z)=h(z^-1), define

    Lh(z)=u(z)[h(vz)-h(z)]+u(z^-1)[h(v^-1z)-h(z)],
    u(z)=(1-Az)(1-Bz)(1-Cz)(1-Dz)
                               /[(1-z^2)(1-vz^2)].  (2)

This maps symmetric Laurent polynomials of degree <=k to the same
space. At z=+/-1 the apparent residues cancel because symmetry gives
h(vz)=h(v^-1z). At z^2=v^-1 the first difference vanishes, because
vz=z^-1; the inverse poles cancel in the same way. There are no
other finite poles. At infinity its leading-degree multiplier is

    lambda_k=(v^-k-1)(1-Pv^(k-1)).                   (3)

Indeed u(z)->P/v and u(z^-1)->1. Operator (2) is visibly symmetric
in its four parameters.

Define M_k(z)=(Az,A/z;v)_k. A DIRECT calculation gives

    L M_k=lambda_k M_k+mu_k M_(k-1),
    mu_k=(1-v^-k)(1-ABv^(k-1))
                    (1-ACv^(k-1))(1-ADv^(k-1)).     (4)

Here M_0=1 and the second term is absent for k=0. To prove the
bandwidth in (4), evaluate at z=A^-1v^-j, j=0,...,k-2.
Both shifted M_k vanish; at j=0 the otherwise exceptional forward
term is killed by 1-Az in u(z). Symmetry supplies the reciprocal
zeros. Thus L M_k is divisible by M_(k-1), and the degree bound
leaves only the two terms in (4). The leading term is (3).

For its last coefficient evaluate at z_*=A^-1v^(-(k-1)). Only the
backward shift survives, also when k=1. The exact product ratio is

    M_k(v^-1z_*)/M_(k-1)(z_*)
      =(1-v^-k)(1-A^2v^(2k-2))(1-A^2v^(2k-1))
                                             /(1-A^2v^(k-1)).

Multiplication by u(z_*^-1) cancels these three A^2 factors and
gives mu_k in (4). This proves the operator action from finite
products, rather than citing a polynomial family.

## 2. The finite eigenpolynomial is symmetric in all four parameters

Put

    P_n^(A)(z)=A^-n(AB,AC,AD;v)_n
       *sum_(k=0)^n (v^-n,Pv^(n-1);v)_k v^k M_k(z)
                              /(v,AB,AC,AD;v)_k.     (5)

Its consecutive coefficient ratio is

    v(1-v^(k-n))(1-Pv^(n+k-1))
       /[(1-v^(k+1))(1-ABv^k)(1-ACv^k)(1-ADv^k)]
      =(lambda_n-lambda_k)/mu_(k+1).

Consequently (4) proves L P_n^(A)=lambda_n P_n^(A), with the
terminating endpoint respected. Its leading z^n coefficient is

    (Pv^(n-1);v)_n,                                 (6)

independent of which of A,B,C,D was chosen as first parameter.
This follows by cancelling
(v^-n;v)_n=(-1)^n v^[-n(n+1)/2](v;v)_n against the leading
M_n coefficient (-A)^n v^[n(n-1)/2].

For generic parameters all lambda_0,...,lambda_n are distinct.
The operator is triangular in Laurent degree; hence its degree-n
eigenpolynomial with prescribed leading coefficient (6) is UNIQUE.
Since (2) and (6) are symmetric, (5) is invariant under every
permutation of A,B,C,D. This is purely finite-dimensional linear
algebra. Clearing denominators extends the resulting identity as a
rational identity to all parameter values where its two finite sums
are defined.

## 3. Specialization gives exactly (1)

Set A^2=bc, B=d/A, C=e/A, D=f/A and z=b/A. Then Az=b, A/z=c,
AB=d, AC=e, AD=f, and P v^(n-1)=a by the balance condition.
Exchange A and B in (5). The new numerator pair is d/c,d/b and
the new denominator pair is de/(bc),df/(bc)=av^(1-n)/e.
Thus the factor relating the two sums is

    (bc/d)^n(de/(bc),av^(1-n)/e;v)_n/(e,f;v)_n.

Reverse the latter Pochhammer by
(av^(1-n)/e;v)_n=(-a/e)^n v^[-n(n-1)/2](e/a;v)_n,
and use f=abc v^(1-n)/(de). This is exactly the factor in (1).
The temporary square root A has disappeared. This proves (1).

## 4. The trivalent root parameters and their denominator scope

For a=max(a,b,c), n=b+c-a, and Q^N=1 with
0<=a,b,c<=floor((N-1)/2), the candidate long series is

    4phi3(Q^-n,Q^(a+1),Q^-b,Q^-c;
                    Q^(a-b+1),Q^(a-c+1),Q^(-b-c);Q,Q).

Take the retained parameter called a in (1) to be Q^-b and choose
d=Q^(-b-c), e=Q^(a-b+1). Formula (1) gives the short series

    4phi3(Q^-n,Q^-b,Q^-b,Q^(-J-1);
                  Q^(-b-c),Q^(-b-c),Q^(-2b);Q,Q),
    J=a+b+c.

On the saturation domain delta=J-(N-1)>=0, Q^(-J-1)=Q^-delta.
Thus it terminates at min(n,delta). None of the displayed
denominators reaches its first zero: n<=min(b,c), b+c<N and
2b<N. The positive starting denominators in the long sum also
remain below N. The finite identity therefore specializes directly;
no discarded root residue or choice of a generic normal germ is
required. Converting either series to an ACTUAL trivalent source
still requires the separate source/Euler coefficient calculation.

Audit: [finite operator, rational Sears and actual root parameter checks](../experiments/audit_finite_balanced_sears_operator_proof.py).

The finite operator proof establishes the balanced Sears identity. Exact operator, generic balanced-identity and supported-root-family checks supplement that proof.