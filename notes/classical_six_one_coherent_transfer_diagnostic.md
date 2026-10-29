# Coherent classical 6_1 transfer versus the pointwise root envelope

28 October 2026. This is a numerical diagnostic for a CLASSICAL
companion product. It does not construct the actual quantum operator,
transport the original ordinary-color source, or establish an upper
bound for the Kashaev invariant.

Use Y=exp(2 pi i x) and the supplied peripheral quartic

    A(Y,L)=Y^4 L^4
       +(-Y^8+Y^7+3Y^4+3Y^3-2Y^2)L^3
       +(Y^8-3Y^7-Y^6+3Y^5+6Y^4+3Y^3-Y^2-3Y+1)L^2
       +(-2Y^6+3Y^5+3Y^4+Y-1)L+Y^4.             (1)

Writing its coefficients as a_4,...,a_0, take the forward companion

    T(x)=[[0,1,0,0],[0,0,1,0],[0,0,0,1],
          [-a_0/a_4,-a_1/a_4,-a_2/a_4,-a_3/a_4]].

The tested product has its later time on the left:

    P_N=T((N-1)/N)...T((N/2)/N).                 (2)

Thus it advances the state (u_j,u_(j+1),u_(j+2),u_(j+3)) along
the half color orbit. It starts at the actual classical degeneracy
A(-1,L)=(L-1)^4. The leading coefficient Y^4 never vanishes on
this circle. At x=5/6 the polynomial divided by Y^4 is

    L^4+5L^3+15L^2+5L+1,

whose two expanding roots are distinct conjugates with equal modulus.
The pointwise spectral radius therefore permits a modulus-only
switch there; it does not require a coherent solution to make that
switch.

For overflow control, each matrix multiplication is followed by
division by its Frobenius norm and addition of that norm's logarithm
to a scalar accumulator. The final largest singular value restores
the operator norm. This is an exact rescaling algorithm up to the
stated arithmetic precision. A Frobenius norm by itself would give
the same exponential rate, since the two norms differ by at most 2.

| N | Working decimal digits, cross-checked | log(||P_N||_2)/N |
|---|---|---|
| 128 | 100 and 164 | 0.52892850040928923661 |
| 256 | 100 and 164 | 0.51813210696801742082 |
| 512 | 171 and 257 | 0.51234403519576993241 |
| 1024 | 342 and 513 | 0.50841759797754220015 |

Both the accumulated log norm and the normalized final matrix agree
between the paired runs beyond the 80 stored decimal digits. In
particular the lower precision is always at least max(100,N/3),
rather than a fixed precision that could seed a wrong expanding
channel as N grows.

For comparison, direct root quadrature gives

    integral_(1/2)^1 log rho(T(x)) dx
                  =0.5482868866186796             (3)

with the reported numerical integration error 1.9e-10. The coherent
rates are already below (3) and move toward the separately proposed
maximal branch-action rate approximately 0.50356, rather than toward
(3). This supplies concrete evidence that the scalar spectral-radius
envelope loses important phase information for this quartic.

The finite data do not prove the limiting product rate, exclude
different subsequence behavior, or justify replacing the classical
matrices by an actual quantum recurrence. Even a proved classical
product estimate would still require uniform control of that
replacement and the original complex source packet. The independently
proved whole-source spectral theorem retains its safe envelope;
this diagnostic identifies a plausible improvement to investigate.

[Reproducible computation](../experiments/diagnostic_six_one_coherent_classical_transfer.py)
and [stored results](../experiments/six_one_coherent_classical_transfer_results.json).
