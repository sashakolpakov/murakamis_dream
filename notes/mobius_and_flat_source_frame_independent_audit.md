# Independent audit of the Möbius framing fiber and flat source frame

27 October 2026. Independent proof audit of
[the Möbius framing and norm-pole theorem](mobius_fourier_framing_and_intrinsic_norm_pole.md)
and [the flat cyclic source-frame theorem](flat_cyclic_source_frame_and_scalar_period.md).
The substantive algebraic claims pass. The derivative and base-ring
qualifications below should be retained. No new selected-period
comparison follows merely from these source-frame identifications.

## 1. The actual prefix Möbius formula and its orientation pass

Factor U-V=u v, with v=(a,b) and w=v V inverse=(c,d). Since
U,V have determinant one and UV inverse is nontrivial trace two,
w u=0 and U-V has rank exactly one. In the actual F(r,s) frame,
the first row of F inverse(U-V)F is proportional to vF. Using
the inverse of the determinant-one matrix F inverse V F gives

\[
 \frac p\sigma
  =\frac{(vF)_2\ell_V-(vF)_1(V')_{12}}{(vF)_1}
  =\frac{(wF)_2}{(vF)_1}
  =\frac{c(1-r)-ds}{ar+bs}.
\]

This verifies the full prefix adapter and its sign directly,
without a position-discriminant square root. Solving gives the
displayed inverse, and differentiating gives

\[
 r_p=\frac{\sigma[s(ad-bc)-ac]}{(ap+\sigma c)^2}.
\]

The two-form orientation also passes. Since
Omega_cut=-dr wedge ds/[s(1+s)] and d log A=-ds/(1+s), the
coefficient of d log A wedge d log p is -p r_p/s, exactly the
negative sign in the theorem. In the finite-pole chart the
projective pole is lambda=-sigma c/a, independent of s. On
c_U-c_V nonzero its trace-word expression follows from
c_U-c_V=u_2 a and c_(UV inverse)=u_2 c. This is intrinsic to
the MARKED prefix/cut data, not an asserted diagram-independent
topological invariant.

The actual figure-eight prefix factorization gives v=(1,2),
w=(1+u,1), sigma=-1, and the theorem's numerator, inverse and
derivative follow. Its pole lambda=1+u=-u squared has order six
at either geometric embedding. This agrees with the independently
computed exceptional-fiber limit gamma_0=u squared: its pole
p=-gamma_0 is the same point. The finite- and infinite-pole
charts in the proof retain their nonvanishing hypotheses correctly.

## 2. The finite cyclic norm and the required derivative qualification

The rational identity

\[
 \frac1N\sum_{p^N=1}\frac p{(p-\lambda)^2}
       =\frac{N\lambda^{N-1}}{(1-\lambda^N)^2}
\]

follows by differentiating the finite partial-fraction expansion
of 1/(1-lambda^N), or directly from the companion matrix. It
has the theorem's sign and exponent. The pole-at-zero and
pole-at-infinity averages vanish for N greater than one. For
fixed nonzero G and absolute lambda not one, (1/N) log absolute
value of G N lambda^(N-1)/(1-lambda^N)^2 tends to minus the
absolute value of log absolute lambda. Hence a rational fiber
coordinate does not itself force a subexponential source weight.

For the WHOLE product P_N(Q,lambda), the derivative must be written

\[
 D_Q\log P_N
      =\sum_{j=0}^{N-1}\frac{j\lambda Q^{-j}}{1-\lambda Q^{-j}},
 \qquad D_QP_N=P_N D_Q\log P_N.                             \tag{1}
\]

The sum alone is the logarithmic derivative, not D_Q P_N. This
minor wording correction was reported to the author. At a norm-zero
fiber neither the apparent logarithmic poles nor their product
with P_N should be evaluated separately: use the original finite
product derivative. The root relation P_N=1-lambda^N is not an
identity of its Q-normal extension.

For N divisible by six the actual figure-eight principal-density
sampling encounters its pole. The actual finite tensor remains
regular. This is an explicit reason the rational principal-density
average cannot be declared the whole selected source. It is not
a statement that the original invariant or its selected geometric
coefficient is singular or zero.

## 3. The source-cyclic classification is scheme-theoretic on its chart

The flat-frame argument is valid over COMMUTATIVE base algebras,
including those with nilpotents. The orbit map from N copies of
the source line is its explicit open-chart hypothesis. In that
line-valued frame AP=A fixes A to the summing source and P to
the cyclic shift; BA=A fixes the zeroth column of B. The remaining
rows of the aligned defect give B_(i,j+1)=Q B_(i-1,j). Their wrap
equations force every off-diagonal zeroth-row entry to zero,
and hence B=diag(1,Q,...,Q^(N-1)). This uses no delta division.

The line-bundle groupoid and the removal of its automorphisms by
a nonzero marked source vector follow from this canonical frame.
They do not classify unrelated noncyclic components. Distinct root
eigenvalues prove the orbit hypothesis in a neighborhood of the
actual primitive-root source, as stated.

The additional aligned defect projector is e_0 rho with rho_0=1.
The whole multiplicative equation becomes exactly delta rho_j=0.
If delta is a nonzero divisor on the base, its flat saturation is
the actual e_00 projector and no extra row parameters remain.
The statement that saturation is JUST the original base has this
necessary scope. On a base with delta-torsion it also removes base
torsion: for example delta=epsilon in k[epsilon]/epsilon squared
makes delta-power saturation the zero ring. This qualification was
reported and is now explicit in the current note. It does not affect
the actual regular normal coefficient ring or the preceding
classification over arbitrary commutative bases.

## 4. The whole corrected algebra and the nonaligned family pass

Evaluation at Q^j makes tau(X)=Q inverse times (X-delta e_0(X))
the predecessor cyclic permutation of the actual clock nodes.
Thus tau(e_j)=e_(j+1), with the theorem's orientation. In its
crossed product the elements e_i P^(i-j) multiply as E_ij and
give exactly Mat_N of the base. In particular its whole correction
retains the finite wrap rather than imposing the inconsistent
generic-Q relation BP=QPB with P^N=I.

The explicit N=2 nonaligned family also passes. Set h=Q-Q inverse.
Its conditions reduce to t squared=x(1+x); then its multiplicative
commutator entries agree exactly with the displayed R. Replacing
delta by delta^k in x and t preserves this identity and makes the
tilt invisible to any prescribed fixed jet, while changing B's
second eigenvalue. The moving projector image fails alignment
with the actual source line. This is a valid counterexample to
omitting WHOLE alignment, not to the positive aligned theorem.

The scalar-intertwiner conclusion is exact. Root actual closure
with generic meridian M is scalar; the auxiliary whole q-normal
lift need not be, as the earlier literal unknot calculation shows.
The current note explicitly retains that scope when mentioning an
actual scalar knot transport. A central scalar is not fixed by source-frame
classification. Strictly requiring the FINAL transport to fix the
source vector would set that scalar to one and would be an extra
normalization, not a property of the original period.

## 5. The central loop identity is exact but needs a typed endpoint map

The [actual framed loop/source identity](actual_rank_one_multiplicative_moment_and_orbit_source.md),
equation (5a), follows from Delta_mom S_P=Q(Z inverse minus one)Q_0
and Q_0=v ell. It is an exact whole rank-one insertion factorization,
with selected divided-normal insertion Q_N Q_0. Its orbit path and
source mark are necessary.

It does not by itself identify a geometric endpoint crossing. Its
normal divisor is 1-Q^N. The Möbius framing pole has norm divisor
1-lambda^N, which is generally NONZERO at that same actual root.
Even when both vanish at a resonant level, their extensions and
normal orders are independent until an actual word/source map
compares them. No such identification follows from (5a) or from
the rigidity of the finite source frame.

Algebraically (5a) is homogeneous under arbitrary central rescalings
of C_1 and C_2; their scalar periods rescale on both sides. With
C_2=I it prescribes the inserted period in terms of the already
unknown uninserted one, rather than determining that unknown scalar.
A genuine endpoint comparison must additionally transport the actual
crossing word, co-source, orbit path and normal divisor into the
geometric relative endpoint complex. The audited notes correctly
leave this selected comparison and the volume limit open.
